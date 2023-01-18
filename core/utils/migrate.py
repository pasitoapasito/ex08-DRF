import json

from background_task import background

from config.settings import REDIS_HOSTNAME
from core.utils.queue import RedisQueue

wating_queue: RedisQueue = RedisQueue(
    'wating',
    host=f'{REDIS_HOSTNAME}',
    port=6379,
    db=1,
)

participating_queue: RedisQueue = RedisQueue(
    'participating',
    host=f'{REDIS_HOSTNAME}',
    port=6379,
    db=1,
)


class MigrateParticapant:

    @background(schedule=1)
    def data_migrate() -> None | str:
        wating_queue.clear()
        participating_queue.clear()
        try:
            for i in range(100):
                element = json.loads(wating_queue.get(block=True, timeout=180))
                if not element:
                    break
                element['participant'] = i+1
                participating_queue.put(json.dumps(element))
            else:
                print('대기열 큐에서 참가열 큐로 데이터 마이그레이션을 성공했습니다.')
                return None
        except Exception as e:
            wating_queue.clear()
            participating_queue.clear()
            print(e)
            return '대기열 큐에서 참가열 큐로 데이터 마이그레이션을 실패했습니다.'
