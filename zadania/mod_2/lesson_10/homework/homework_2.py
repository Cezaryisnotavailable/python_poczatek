
def any_length_kwargs(**kwargs):
    call_str = "print_call_str("
    for arg_name, arg_value in kwargs.items():
        call_str += f"{arg_name}={arg_value}, "
    call_str += ")"
    print(call_str)


def run_homework():


    any_length_kwargs(argument="Mikołaj", wiek=134)

if __name__ == "__main__":
    run_homework()