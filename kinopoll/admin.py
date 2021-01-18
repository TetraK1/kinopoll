from django.contrib import admin

from .models import Poll, Question, Response, Answer
from .models import TextQuestion, TextAnswer
from .models import MultipleChoiceQuestion, MultipleChoiceOption, MultipleChoiceAnswer
from .models import RankedQuestion, RankedOption, RankedAnswer

# Register your models here.
admin.site.register(Poll)
#admin.site.register(Question)
admin.site.register(Response)
#admin.site.register(Answer)

admin.site.register(TextQuestion)
admin.site.register(TextAnswer)

admin.site.register(MultipleChoiceQuestion)
admin.site.register(MultipleChoiceOption)
admin.site.register(MultipleChoiceAnswer)

admin.site.register(RankedQuestion)
admin.site.register(RankedOption)
admin.site.register(RankedAnswer)