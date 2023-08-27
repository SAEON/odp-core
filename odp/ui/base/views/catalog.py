import json
from random import randint

from flask import Blueprint, current_app, redirect, render_template, request, url_for

from odp.const import ODPMetadataSchema
from odp.ui.base import api, cli
from odp.ui.base.forms import SearchForm

bp = Blueprint('catalog', __name__)


@bp.app_template_filter()
def doi_title(doi: str) -> str | None:
    """Get the title for the given DOI."""
    if cached_title := cli.cache.get(doi, 'title'):
        return cached_title

    catalog_id = current_app.config['CATALOG_ID']
    title = cli.get(
        f'/catalog/{catalog_id}/getvalue/{doi}',
        schema_id=ODPMetadataSchema.SAEON_DATACITE4,
        json_pointer='/titles/0/title',
    )
    # titles rarely change, but we must expire them in case they ever do;
    # keep for between 7 and 14 days, so a large set of child record titles doesn't expire all at once
    cli.cache.set(doi, 'title', value=title, expiry=randint(604800, 1209600))

    return title


@bp.route('/')
@cli.view()
def index():
    catalog_id = current_app.config['CATALOG_ID']
    facets = current_app.config['CATALOG_FACETS']

    text_query = request.args.get('q')
    north_bound = request.args.get('n')
    east_bound = request.args.get('e')
    south_bound = request.args.get('s')
    west_bound = request.args.get('w')
    start_date = request.args.get('after')
    end_date = request.args.get('before')
    exclusive_region = request.args.get('exclusive_region')
    exclusive_interval = request.args.get('exclusive_interval')
    sort = request.args.get('sort', 'rank desc')
    page = request.args.get('page', 1)

    facet_api_query = {}
    facet_ui_query = {}
    facet_fields = {}
    for facet_title in facets:
        facet_field = SearchForm.facet_fieldname(facet_title)
        facet_fields[facet_title] = facet_field
        if facet_value := request.args.get(facet_field):
            facet_api_query[facet_title] = facet_value
            facet_ui_query[facet_field] = facet_value

    result = cli.get(
        f'/catalog/{catalog_id}/search',
        text_query=text_query,
        facet_query=json.dumps(facet_api_query),
        north_bound=north_bound,
        east_bound=east_bound,
        south_bound=south_bound,
        west_bound=west_bound,
        start_date=start_date,
        end_date=end_date,
        exclusive_region=exclusive_region,
        exclusive_interval=exclusive_interval,
        sort=sort,
        page=page,
        size=25,
    )

    return render_template(
        'catalog_index.html',
        form=SearchForm(request.args),
        result=result,
        facet_fields=facet_fields,
    )


@bp.route('/search', methods=('POST',))
def search():
    form = SearchForm(request.form)
    query = form.data
    query.pop('csrf_token')
    if not query['exclusive_region']:
        query.pop('exclusive_region')
    if not query['exclusive_interval']:
        query.pop('exclusive_interval')

    facets = current_app.config['CATALOG_FACETS']
    for facet_title in facets:
        if not query[facet_field := SearchForm.facet_fieldname(facet_title)]:
            query.pop(facet_field)

    return redirect(url_for('.index', **query))


@bp.route('/<path:id>')
@cli.view()
@api.user()
def view(id):
    catalog_id = current_app.config['CATALOG_ID']

    record = cli.get(f'/catalog/{catalog_id}/records/{id}')
    sdg_vocab = {
        keyword_obj['id']: keyword_obj['data']
        for keyword_obj in cli.get(f'/vocabulary/SDG')['terms']
    }

    return render_template(
        'catalog_record.html',
        record=record, sdg_vocab=sdg_vocab,
    )
