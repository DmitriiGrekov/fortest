from questions.forms import AddSubjectForm
from accounts.forms import UserRegisterForm, LoginForm
from questions.models import SubjectModel


def context_proc(request):
    if request.user.is_authenticated:
        subject = SubjectModel.objects.filter(author=request.user)

        if request.user.current_subject:

            current_subject_user = request.user.current_subject
        else:
            current_subject_user = None
        if current_subject_user:

            count_questions = len(current_subject_user.questions.all())
            count_user_questions = len(request.user.all_questions.all())
        else:
            count_questions = 0
            count_user_questions = 0
        # if len(request.user.current_subject.questions.all()) == 0:
        #     no_questions = 'По данному предмету нет вопросов'
        # else:
        #     no_questions = None
        return {'add_subject': AddSubjectForm,
                'subjects': subject,
                'current_subject_user': current_subject_user,
                'count_questions': count_questions,
                'count_user_questions': count_user_questions,
                # 'no_questions': no_questions
                }

    return {'login_form': LoginForm,
            'reg_form': UserRegisterForm,
            'add_subject': AddSubjectForm}
    return