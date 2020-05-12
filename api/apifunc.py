def validate_finite_values_entity(values, supported_values, invalid_trigger, key, support_multiple, pick_first):
    partially_filled = False
    trigger = ''
    keySet = set()
    temp = True if len(values) == 0 else False
    ids = []
    for val in values:
        value = val["value"]
        if support_multiple:
            if value in supported_values:
                ids.append(value.upper())
            else:
                temp = True
        if value in supported_values:
            keySet.add(value)
    filled = True if len(ids)>0 and len(ids) == len(values) else False
    if len(values)>0 and not filled:
        partially_filled = True
    params = {
        key : ids[0] if pick_first and len(ids)>0 else ids
    }
    dicti = {
        "filled": filled,
        "partially_filled": partially_filled,
        "trigger": trigger,
        "parameters": params
    }
    if temp and not pick_first:
        dicti["parameters"] = {}
        dicti["trigger"] = invalid_trigger
        return dicti
    if temp and pick_first:
        if len(ids) == 0:
            dicti["trigger"] = invalid_trigger
            return dicti
    return dicti


def validate_numeric_entity(values, invalid_trigger,pick_first):
    filled = False
    params = {}
    partially_filled = False
    trigger = ''
    keySet = set()
    temp= True if len(values) == 0 else False
    ages = []
    ages1 = []
    for val in values:
        entity_type = val["entity_type"]
        value = val["value"]
        if value>0:
            ages.append(value)
        if value>=18 and value<=30:
            ages1.append(value)
        else:
            temp = True
    filled = True if len(ages)>0 and len(ages) == len(values) else False
    if len(values)>0 and not filled:
        partially_filled = True
    if len(ages1)> 0 and len(ages) != len(ages1):
        trigger = invalid_trigger
        params = {
            "age_stated": max(ages1)
        }
    if len(ages1)> 0 and len(ages) == len(ages1):
        params = {
            "age_stated": max(ages1)
        }
    dicti = {
        "filled" : filled,
        "partially_filled": partially_filled,
        "trigger": trigger,
        "parameters": params
    }
    if temp and not pick_first:
        dicti["trigger"] = invalid_trigger
        return dicti
    if temp and pick_first:
        if len(ages) == 0:
            dicti["trigger"] = invalid_trigger
            return dicti
    return dicti

