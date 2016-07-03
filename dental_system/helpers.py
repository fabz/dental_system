def set_attributes(update_data, model_obj):
    for key in update_data.keys():
        setattr(model_obj, key, update_data[key])