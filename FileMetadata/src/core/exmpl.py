def getSize(file_info):
	"""
	@parapm file_info {FileInfo}
	"""
	size = file_info.stat.size()
	if size == 0:
		try:
			size = computeSize(file_info.file)
		except Exception:
			pass
	return size

# ---------------------
def computeSize(file):
	old_file_position = file.tell()
	file.seek(0, os.SEEK_END)
	size = file.tell()
	file.seek(old_file_position, os.SEEK_SET)
	return size

 # -------------------

# GetOwner()

 # if win32
 # sdjssjg
 # else : unix ghskjgkjhg