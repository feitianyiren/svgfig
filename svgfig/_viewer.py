#!/usr/bin/env python                                                                                                                                                              
import cairo
import rsvg
import gtk

class View:
	def __init__(self):
		self.string = """<svg width="800" height="600"></svg>"""
		self.win = gtk.Window()
		self.da = gtk.DrawingArea()
		self.win.add(self.da)
		self.da.set_size_request(800, 600)
		self.da.connect("expose-event", self.expose_cairo)
		self.win.show_all()
		self.win.present()
	def expose_cairo(self, win, event):
		svg = rsvg.Handle(data=self.string)
		cr = self.da.window.cairo_create()
		svg.render_cairo(cr)
	def renderSVG(self, text):
		x, y, w, h = self.win.allocation
		self.da.window.invalidate_rect((0,0,w,h), False)
		self.string = text
