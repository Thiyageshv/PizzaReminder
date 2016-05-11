class yelp(object):
	def __init__(self, **kwargs):
        	for field in ('name', 'res',):
            		setattr(self, field, kwargs.get(field, None))


