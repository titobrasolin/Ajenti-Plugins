# -*- coding: utf-8 -*-
from ajenti.api import *
from ajenti.plugins.main.api import SectionPlugin
from ajenti.ui import on
from ajenti.ui.binder import Binder

@plugin
class SanickioskScreensaverPrefs (SectionPlugin):
	default_classconfig = {
		'photos_enable': False,
	}
	classconfig_root = True

	def init(self):
		self.title = 'Режим Снимки'
		self.icon = 'picture'
		self.category = 'Kiosk'

		self.append(self.ui.inflate('kiosk_photos:main'))
		self.binder = Binder(self, self)
		self.binder.populate()

	@on('save', 'click')
	def save(self):
		self.binder.update()
		self.save_classconfig()
		self.context.notify('info', _('Настройките са запаметени. Моля, рестартирайте киоска.'))
		self.binder.populate()

		all_vars = '\n'.join([k + '="' + str(v) + '"' for k,v in self.classconfig.iteritems()])
		open('/home/kiosk/.kiosk/photos.cfg', 'w').write(all_vars) #save

