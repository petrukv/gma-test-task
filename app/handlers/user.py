import logging

from peewee import DoesNotExist
from aiohttp import web

from app.models import ApiUser


logger = logging.getLogger(__name__)

async def create_user(request):
    data = await request.json()
    try:
        user = ApiUser.create(name=data['name'], email=data['email'], password=data['password'])
        logger.info(f"User created with ID {user.id}")
        return web.json_response({'id': user.id})
    except Exception as e:
        logger.error(f"Error creating user: {str(e)}")
        return web.json_response({'error': str(e)}, status=400)

async def get_user(request):
    user_id = int(request.match_info['user_id'])
    try:
        user = ApiUser.get(ApiUser.id == user_id)
        logger.info(f"User retrieved with ID {user_id}")
        return web.json_response({'id': user.id, 'name': user.name, 'email': user.email})
    except DoesNotExist:
        logger.warning(f"User with ID {user_id} not found")
        return web.json_response({'error': 'User not found'}, status=404)
