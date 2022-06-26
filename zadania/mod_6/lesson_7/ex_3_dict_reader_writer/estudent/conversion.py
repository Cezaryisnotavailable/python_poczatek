def str_to_bool(str_bool):
    if str_bool == "True":
        return True
    elif str_bool == "False":
        return False
    raise ValueError(f" {str_bool} To niepoprawna wartość dla typu bool, typ {type(str_bool)}")