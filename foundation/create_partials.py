

import glob
import os


def content(fname):
	return '''// Foundation by ZURB
// foundation.zurb.com
// Licensed under MIT Open Source

@import 'partial';
@import '../scss/foundation/components/%s';
''' % fname


for fname in glob.glob('static/foundation/scss/foundation/components/*.scss'):
	fname = os.path.basename(fname)
	fname, ext = os.path.splitext(fname)
	fname = fname[1:]
	filename = 'static/foundation/partial-scss-rtl/%s.scss' % fname
	print filename,
	if os.path.exists(filename):
		print 'file exist, omitting.'
	else:
		with open(filename, 'w') as f:
			f.write(content(fname));
			print 'Created.'

