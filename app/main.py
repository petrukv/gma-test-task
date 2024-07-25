import logging

from aiohttp import web

from handlers.location import create_location, get_location
from handlers.user import create_user, get_user
from handlers.device import create_device, get_device, update_device, delete_device
from models import db, ApiUser, Device, Location


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


logger.info("Connecting to the database...")
db.connect()
db.create_tables([ApiUser, Device, Location])
logger.info("Database connected and tables created")

logger.info("Starting the application...")


app = web.Application()
app.add_routes([
    web.post('/locations', create_location),
    web.get('/locations/{location_id}', get_location),

    web.post('/users', create_user),
    web.get('/users/{user_id}', get_user),

    web.post('/devices', create_device),
    web.get('/devices/{device_id}', get_device),
    web.put('/devices/{device_id}', update_device),
    web.delete('/devices/{device_id}', delete_device)
])

if __name__ == '__main__':
    logger.info("Application started")
    web.run_app(app, port=8080)
