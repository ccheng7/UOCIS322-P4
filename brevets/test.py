import arrow 
import nose
import logging
import acp_times
import sys
logging.basicConfig(format = '%(levelname)s:(message)s',level = logging.WARNING
log = logging.getLogger(__name__)
sys.path.append("..")

def test_brevet_dist_time_200():
    time = arrow.now()
    assert acp_times.open_time(0, 200, time) == time
    assert acp_times.close_time(0, 200, time) == time.shift(hours = 1)
    assert acp_times.open_time(20, 200, time) == time.shift(minutes = 35)
    assert acp_times.close_time(20, 200, time) == time.shift(hours = 2)
    assert acp_times.open_time(60, 200, time) == time.shift(hours =1 , minutes =46)
    assert acp_times.close_time(60, 200, time) == time.shift(hours = 4)




def test_brevet_dist_time_300():
    time = arrow.now()
    assert acp_times.open_time(0, 300, time) == time
    assert acp_times.close_time(0, 300, time) == time.shift(hours = 1)
    assert acp_times.open_time(100, 300, time) == time.shift(hours =56,minutes = 35)
    assert acp_times.close_time(100, 300, time) == time.shift(hours = 6, minutes =40)
    assert acp_times.open_time(200, 300, time) == time.shift(hours =5 , minutes =53)
    assert acp_times.close_time(200, 300, time) == time.shift(hours =13 , minutes =20)



def test_brevet_dist_time_400():
    time = arrow.now()
    assert acp_times.open_time(0, 400, time) == time
    assert acp_times.close_time(0, 400, time) == time.shift(hours = 1)
    assert acp_times.open_time(200, 400, time) == time.shift(hours =5 , minutes = 53)
    assert acp_times.close_time(200, 400, time) == time.shift(hours = 13, minutes =20)
    assert acp_times.open_time(300, 400, time) == time.shift(hours =9)
    assert acp_times.close_time(300, 400, time) == time.shift(hours = 20)


def test_brevet_dist_time_600():
    time = arrow.now()
    assert acp_times.open_time(0, 600, time) == time
    assert acp_times.close_time(0, 600, time) == time.shift(hours = 1)
    assert acp_times.open_time(200, 600, time) == time.shift(hours =5,minutes = 53)
    assert acp_times.close_time(200, 600, time) == time.shift(hours = 13, minutes =20)
    assert acp_times.open_time(300, 600, time) == time.shift(hours =9)
    assert acp_times.close_time(300, 600, time) == time.shift(hours = 20)


def test_brevet_dist_time_1000():
    time = arrow.now()
    assert acp_times.open_time(0, 1000, time) == time
    assert acp_times.close_time(0, 1000, time) == time.shift(hours = 1)
    assert acp_times.open_time(200, 1000, time) == time.shift(hours= 5,minutes =53)
    assert acp_times.close_time(200, 1000, time) == time.shift(hours = 13, minutes = 20)
    assert acp_times.open_time(300, 1000, time) == time.shift(hours =9)
    assert acp_times.close_time(300, 1000, time) == time.shift(hours = 20)


