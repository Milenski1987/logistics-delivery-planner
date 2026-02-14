from typing import Dict, Any


class ReadOnlyFieldsMixin:
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].disabled = True


class ModifyFormData:
    def get_form_kwargs(self) -> Dict[str, Any]:
        kwargs = super().get_form_kwargs()
        kwargs['data'] = self.request.GET

        return kwargs