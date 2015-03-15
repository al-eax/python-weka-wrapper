# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# container.py
# Copyright (C) 2015 Fracpete (pythonwekawrapper at gmail dot com)

from weka.core.dataset import Instances


class Container(object):
    """
    Container for storing multiple objects and passing them around together in the flow.
    """

    def __init__(self):
        """
        Initializes the container.
        """
        self._data = {}
        self._allowed = []

    def get(self, name):
        """
        Returns the stored data.
        :param name: the name of the item to return
        :type name: str
        :return: the data
        :rtype: object
        """
        return self._data[name]

    def set(self, name, value):
        """
        Stores the given data (if not None).
        :param name: the name of the item to store
        :type name: str
        :param value: the value to store
        :type value: object
        """
        if value is not None:
            self._data[name] = value

    @property
    def allowed(self):
        """
        Returns the all the allowed keys.
        :return: the list of allowed keys.
        :rtype: list
        """
        return self._allowed

    def is_valid(self):
        """
        Checks whether the container is valid.
        :return: True if the container is valid
        :rtype: bool
        """
        return True

    def __str__(self):
        """
        Returns the content of the container as string.
        :return: the content
        :rtype: str
        """
        return str(self.data)


class ModelContainer(Container):
    """
    Container for models.
    """

    def __init__(self, model=None, header=None):
        """
        Initializes the container.
        :param model: the model to store (eg Classifier or Clusterer)
        :type model: object
        :param header: the header instances
        :
        """
        super(ModelContainer, self).__init__()
        self.set("Model", model)
        if header is not None:
            header = Instances.template_instances(header)
        self.set("Header", header)

    def is_valid(self):
        """
        Checks whether the container is valid.
        :return: True if the container is valid
        :rtype: bool
        """
        return ("Model" in self._data) or ("Model" in self._data and "Header" in self._data)