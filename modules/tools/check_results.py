from __future__ import absolute_import, print_function

from qgis.PyQt.QtGui import QDockWidget, QTreeWidgetItem, QColor
from PyQt4 import QtCore

from veriso.base.utils.utils import (get_ui_class)
import sip

FORM_CLASS = get_ui_class('check_results.ui')


class CheckResultsDock(QDockWidget, FORM_CLASS):
    """Creates a DockWidget where show the results of the checks.
    The widget is based on TreeWidget component

    """
    result_parent = None

    def __init__(self, iface, parent=None):
        QDockWidget.__init__(self, parent)

        self.setupUi(self)
        self.iface = iface
        self.message_bar = self.iface.messageBar()
        self.layer = None
        self._gui_elements = [
            self.treeWidget
        ]

    def clear_results(self):
        self.treeWidget.clear()

    def add_result(self, fields):
        """Add a parent result
        """
        found_items = self.treeWidget.findItems(fields[0], QtCore.Qt.MatchExactly)
        if len(found_items) > 0:
            self.treeWidget.takeTopLevelItem(self.treeWidget.indexOfTopLevelItem(found_items[0]))

        itm = QTreeWidgetItem(fields)
        if(fields[2]=='OK'):
            itm.setBackgroundColor(2, QColor(0, 255, 0, 127))
        else:
            itm.setBackgroundColor(2, QColor(255, 0, 0, 127))


        self.treeWidget.addTopLevelItem(itm)
        self.result_parent = itm

    def add_child(self, fields):
        """Add a child result to the last inserted parente
        """
        QTreeWidgetItem(self.result_parent, fields)