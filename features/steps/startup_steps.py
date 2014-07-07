
from mock import MagicMock
from mock import patch
import wx

    
@given(u'vpt starts')
def step_impl(context):
    from vpt2 import *
    context.app = wx.App(False)
    context.frame = vptFrame()
    context.frame.Show(True)
    context.pgm = Program()

@then(u'a window with the title \'Virtual Page Turner 2\' should be seen')
def step_impl(context):
    assert context.frame.title == 'Virtual Page Turner 2'

@given(u'there is no prior selection')
def step_impl(context):
    context.frame.priorSelection = None

@when(u'I select a piece')
def step_impl(context):
    with patch('wx.DirDialog.ShowModal',return_value=wx.ID_OK):
        with patch('wx.DirDialog.GetPath',return_value = '/Users/michaeltoth/Desktop/vpt2/sample/Fur Elise'):
            context.frame.selectPiece()            
    
@then(u'the prior selection is set')
def step_impl(context):
    print 'prior selection is ' + context.frame.priorSelection
    assert context.frame.priorSelection != None

@then(u'a Program class exists')
def step_impl(context):
    try:
        context.pgm
    except NameError:
        assert False
