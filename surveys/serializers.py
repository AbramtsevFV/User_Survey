from drf_writable_nested import WritableNestedModelSerializer
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer, IntegerField, CharField, ValidationError
from .models import Survey, Question, Variants, Answer


class CurrentUserDefault(object):

    def set_context(self, serializer_field):
        self.user_id = serializer_field.context['request'].user.id

    def __call__(self):
        return self.user_id

class AnswerSerializer(ModelSerializer):
    user_id = IntegerField(default=CurrentUserDefault())
    survey = SlugRelatedField(queryset=Survey.objects.all(), slug_field='name')
    quest = SlugRelatedField(queryset=Question.objects.all(), slug_field='question')
    variant = SlugRelatedField(queryset=Variants.objects.all(), slug_field='answer_option', allow_null=True)
    variant_text = CharField(max_length=200, allow_null=True, required=False)

    class Meta:
        model = Answer
        fields = '__all__'

    def validate(self, attrs):
        question_type = Question.objects.get(id=attrs['quest'].id).question_type
        try:
            if question_type == 'CHOICE' or question_type == 'TEXT':
                obj = Answer.objects.get(quest=attrs['quest'].id, survey=attrs['survey'], user_id=attrs['user_id'])
            elif question_type == 'MULTICHOICE':
                obj = Answer.objects.get(quest=attrs['quest'].id, survey=attrs['survey'], user_id=attrs['user_id'],
                                         variant=attrs['variant'])
        except Answer.DoesNotExist:
            return attrs
        else:
            raise ValidationError('Already responded')

class VariantsSerializer(ModelSerializer):

    class Meta:
        model = Variants
        fields = ('id', 'question', 'answer_option')

class QuestionSerializer(WritableNestedModelSerializer):
    id = IntegerField(read_only=True)
    variants = VariantsSerializer(many=True)

    class Meta:
        model = Question
        fields = ('id', 'survey', 'question', 'question_type', 'variants')



class Surveyserializers(ModelSerializer):
    id = IntegerField(read_only=True)
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Survey
        fields = ('id', 'name', 'start_date', 'end_date', 'survey_description', 'questions')



    def update(self, instance, validated_data):
        if 'start_date' in validated_data:
            raise ValidationError({'start_date': 'This is an immutable field.'})
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance