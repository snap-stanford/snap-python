  {
	printf "%s.__getitem__ = getitem_vec\n", $1;
	printf "%s.__setitem__ = setitem_vec\n", $1;
	printf "%s.__iter__ = itervec\n", $1;
	printf "%s.__len__ = len_vec\n", $1;
	printf "%s.append = append_vec\n", $1;
	printf "%s.extend = extend_vec\n", $1;
	printf "%s.clear = clear_vec\n", $1;
	printf "%s.insert = insert_vec\n", $1;
	printf "%s.remove = remove_vec\n", $1;
	printf "%s.index = index_vec\n", $1;
	printf "%s.count = count_vec\n", $1;
	printf "%s.pop = pop_vec\n", $1;
	printf "%s.reverse = reverse_vec\n", $1;
	printf "%s.sort = sort_vec\n", $1;
	printf "%s.copy = copy_vec\n", $1;
  }
