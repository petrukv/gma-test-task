import logging

from peewee import DoesNotExist
from aiohttp import web

from app.models import Device, Location, ApiUser


logger = logging.getLogger(__name__)

async def create_device(request):
    data = await request.json()
    try:
        location = Location.get(Location.id == data['location_id'])
        api_user = ApiUser.get(ApiUser.id == data['api_user_id'])
        device = Device.create(
            name=data['name'],
            type=data['type'],
            login=data['login'],
            password=data['password'],
            location=location,
            api_user=api_user
        )
        logger.info(f"Device created with ID {device.id}")
        return web.json_response({'id': device.id})
    except DoesNotExist as e:
        logger.error(f"Error creating device: {str(e)}")
        return web.json_response({'error': str(e)}, status=400)

async def get_device(request):
    device_id = int(request.match_info['device_id'])
    try:
        device = Device.get(Device.id == device_id)
        logger.info(f"Device retrieved with ID {device_id}")
        return web.json_response({
            'id': device.id,
            'name': device.name,
            'type': device.type,
            'login': device.login,
            'password': device.password,
            'location_id': device.location.id,
            'api_user_id': device.api_user.id
        })
    except DoesNotExist:
        logger.warning(f"Device with ID {device_id} not found")
        return web.json_response({'error': 'Device not found'}, status=404)

async def update_device(request):
    device_id = int(request.match_info['device_id'])
    data = await request.json()
    try:
        device = Device.get(Device.id == device_id)
        device.name = data['name']
        device.type = data['type']
        device.login = data['login']
        device.password = data['password']
        device.save()
        logger.info(f"Device updated with ID {device_id}")
        return web.json_response({'status': 'success'})
    except DoesNotExist:
        logger.warning(f"Device with ID {device_id} not found for update")
        return web.json_response({'error': 'Device not found'}, status=404)

async def delete_device(request):
    device_id = int(request.match_info['device_id'])
    try:
        device = Device.get(Device.id == device_id)
        device.delete_instance()
        logger.info(f"Device deleted with ID {device_id}")
        return web.json_response({'status': 'success'})
    except DoesNotExist:
        logger.warning(f"Device with ID {device_id} not found for deletion")
        return web.json_response({'error': 'Device not found'}, status=404)
