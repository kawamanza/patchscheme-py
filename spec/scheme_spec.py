from mamba import description, it, before
from expects import expect, be_above, have_key
from patchscheme.scheme import Scheme
import patchscheme.strategies as st
from datetime import datetime


class PatchPerson(Scheme):
    created_at = st.Suppress()
    updated_at = st.Force(datetime.now)


with description(PatchPerson) as self:

    with before.each:
        self.stored = dict(
            created_at=datetime(2019, 9, 27, 0, 0),
            updated_at=datetime(2019, 9, 27, 0, 0)
        )
        self.payload = {}
        self.payload.update(self.stored)

    with it('should patch using Force and Suppress'):
        now = datetime.now()
        patch = PatchPerson(self.stored, self.payload).map()
        expect(patch).not_to(have_key('created_at'))
        expect(patch).to(have_key('updated_at'))
        expect(patch['updated_at']).to(be_above(now))
