from datetime import datetime
import pytz


def now_utc():
    return datetime.utcnow()


def now_in_timezone(timezone: str):
    tz = pytz.timezone(timezone)
    return datetime.now(tz)


def format_timestamp(dt: datetime):
    return dt.strftime("%Y-%m-%d %H:%M:%S")