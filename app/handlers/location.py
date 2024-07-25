import logging

from peewee import DoesNotExist
from aiohttp import web

from app.models import Location


logger = logging.getLogger(__name__)

async def create_location(request):
    data = await request.json()
    try:
        location = Location.create(name=data['name'])
        logger.info(f"Location created with ID {location.id}")
        return web.json_response({'id': location.id})
    except Exception as e:
        logger.error(f"Error creating location: {str(e)}")
        return web.json_response({'error': str(e)}, status=400)

async def get_location(request):
    location_id = int(request.match_info['location_id'])
    try:
        location = Location.get(Location.id == location_id)
        logger.info(f"Location retrieved with ID {location_id}")
        return web.json_response({'id': location.id, 'name': location.name})
    except DoesNotExist:
        logger.warning(f"Location with ID {location_id} not found")
        return web.json_response({'error': 'Location not found'}, status=404)
