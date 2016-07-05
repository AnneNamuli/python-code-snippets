def data_type(arg):
  if isinstance(arg, str):
    return len(arg)
  elif arg is None:
    return "no value"
  elif isinstance(arg, bool):
    return True if arg == True else False 