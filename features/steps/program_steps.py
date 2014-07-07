
@then(u'nPieces should be zero')
def step_impl(context):
    assert context.pgm.NumberOfPieces() == 0

@when(u'I call GetPieces with a valid file')
def step_impl(context):
    print 'context.pgm.Getpieces returns ' + str(context.pgm.GetPieces('/Users/michaeltoth/Desktop/vpt2/sample/aProgram.txt'))
    assert context.pgm.GetPieces('/Users/michaeltoth/Desktop/vpt2/sample/aProgram.txt')

@then(u'nPieces should be greater than 0')
def step_impl(context):
    assert context.pgm.NumberOfPieces() > 0
