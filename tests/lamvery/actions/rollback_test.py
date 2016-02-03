# -*- coding: utf-8 -*-

from unittest import TestCase
from nose.tools import raises
from mock import Mock, patch

from lamvery.actions.rollback import RollbackAction


def default_args():
    args = Mock()
    args.conf_file = '.lamvery.yml'
    args.dry_run = True

    return args


class RollbackActionTestCase(TestCase):

    @raises(Exception)
    def test_action_function_not_exists(self):
        with patch('lamvery.actions.base.LambdaClient') as c:
            c.get_function_conf = Mock(return_value={})
            c.get_function_conf = Mock(return_value=None)
            action = RollbackAction(default_args())
            action._get_client = Mock(return_value=c)
            action.action()

    @raises(Exception)
    def test_action_previous_version_not_exists(self):
        with patch('lamvery.actions.base.LambdaClient') as c:
            c.get_function_conf = Mock(return_value={'foo': 'bar'})
            c.get_previous_version = Mock(return_value=None)
            action = RollbackAction(default_args())
            action._get_client = Mock(return_value=c)
            action.action()

    def test_action(self):
        with patch('lamvery.actions.base.LambdaClient') as c:
            c.get_function_conf = Mock(return_value={'foo': 'bar'})
            c.get_previous_version = Mock(return_value='1')
            action = RollbackAction(default_args())
            action._get_client = Mock(return_value=c)
            action.action()
