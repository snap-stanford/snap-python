  {
	printf "%s.__getitem__ = getitem_hash\n", $1;
	printf "%s.__setitem__ = setitem_has\n", $1;
	printf "%s.__delitem__ = delitem_hash\n", $1;
	printf "%s.__len__ = len_hash\n", $1;
	printf "%s.__iter__ = iterhash\n", $1;
	printf "%s.clear = clear_hash\n", $1;
	printf "%s.copy = copy_hash\n", $1;
	printf "%s.get = get_hash\n", $1;
	printf "%s.items = items_hash\n", $1;
	printf "%s.keys = keys_hash\n", $1;
	printf "%s.pop = pop_hash\n", $1;
	printf "%s.setdefault = setdefault_hash\n", $1;
	printf "%s.update = update_hash\n", $1;
	printf "%s.values = values_hash\n", $1;
  }
