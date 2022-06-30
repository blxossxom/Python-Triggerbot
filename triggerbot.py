from memory import *
def trigger_bot():
    entity = 0
    while True:
        try:
            if ent.in_game():
                crosshair = lp.get_crosshair_id()
                entity = lp.get_entity_by_crosshair()
                if crosshair == 0 or entity == 0:
                    continue
                    
                local_position = ent.get_position(lp.local_player())
                distance = h.distance(local_position, ent.get_position(entity))
                if ctypes.windll.user32.GetAsyncKeyState(key_handler('triggerbot_key')) and dpg.get_value('triggerbot_checkbox'):
                    if lp.get_team_by_crosshair(entity) != ent.get_team(lp.local_player()) and lp.get_health_by_crosshair(entity) >= 1:
                        if dpg.get_value('humanization_checkbox') == True:
                            v2_delay = round(random.uniform(0.001, 0.01), 3)
                            
                            time.sleep(dpg.get_value('triggerbot_delay') + v2_delay)
                        else:
                            time.sleep(dpg.get_value('triggerbot_delay'))
                        lp.force_attack(6)
