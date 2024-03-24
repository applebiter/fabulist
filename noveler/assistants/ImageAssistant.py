from datetime import datetime
from typing import Type, List, Optional, Union

from sqlalchemy.orm import Session

from noveler.assistants import BaseAssistant
from noveler.models import User, Assistance, Activity


class ImageAssistant(BaseAssistant):
    """Image Assistant

    The Image Assistant is a specialized assistant that uses the Ollama API to
    describe the contents of an image.
    """

    def __init__(self, session: Session, owner: Type[User]):
        super().__init__(session, owner)

        self._name = "Image Assistant"

    def describe(
            self,
            images: List[str],
            prompt: Optional[str] = "Describe the image",
            temperature: Optional[float] = 0.5,
            seed: Optional[int] = None,
            priming: Optional[str] = None,
            options: Optional[dict] = None,
            session_uuid: str = None,
            keep_alive: Optional[Union[float, str]] = None
    ):
        """Describe the contents of an image using the Ollama API.

        Parameters
        ----------
        images : List[str]
            A list of image file paths to be described.
        temperature : Optional[float]
            The temperature to be used when making the request. Defaults to
            0.5.
        seed : Optional[int]
            The seed to be used when making the request. Defaults to None.
        prompt : Optional[str]
            The prompt to be used when requesting the description. Defaults to
            "Describe the contents of the image:".
        priming : Optional[str]
            The priming to be used when describing the image.
        options : Optional[dict]
            The options to be used when making the request.
        session_uuid : str
            The UUID of the session to be used when making the request.
        keep_alive : Optional[Union[float, str]]
            The keep alive value to be used when making the request.
        """
        encoded = []

        for image in images:
            with open(image, "rb") as file:
                encoded.append(file.read())

        if not priming:
            priming = """Image Assistant is ready to describe the image."""

        session_uuid = self._session_uuid if not session_uuid else session_uuid

        if not options:
            options = {
                "temperature": temperature,
                "num_ctx": self._num_ctx
            }

        if not options.get("temperature"):
            options["temperature"] = temperature

        if not options.get("num_ctx"):
            options["num_ctx"] = self._num_ctx

        keep_alive = self._keep_alive if not keep_alive else keep_alive

        with self._session as session:

            try:

                response = self._client.generate(
                    model=self._image_model,
                    prompt=prompt,
                    system=priming,
                    template=self._templates[self._image_model],
                    images=encoded,
                    options=options,
                    keep_alive=keep_alive
                )

                assistance = Assistance(
                    user_id=self._owner.id,
                    session_uuid=session_uuid,
                    assistant=self._name,
                    model=self._image_model,
                    priming=priming,
                    prompt=prompt,
                    temperature=temperature,
                    seed=seed,
                    content=response["response"] if response.get("response") else None,
                    done=response["done"],
                    total_duration=response["total_duration"] if response.get("total_duration") else None,
                    load_duration=response["load_duration"] if response.get("load_duration") else None,
                    prompt_eval_count=response["prompt_eval_count"] if response.get("prompt_eval_count") else None,
                    prompt_eval_duration=response["prompt_eval_duration"] if response.get("prompt_eval_duration") else None,
                    eval_count=response["eval_count"] if response.get("eval_count") else None,
                    eval_duration=response["eval_duration"] if response.get("eval_duration") else None,
                    created=datetime.now()
                )

                summary = f"{self._owner.username} used the Image Assistant"
                activity = Activity(
                    user_id=self._owner.id, summary=summary,
                    created=datetime.now()
                )

                session.add(assistance)
                session.add(activity)

            except Exception as e:
                session.rollback()
                raise e

            else:
                session.commit()
                return response

    def __str__(self):
        return f"Noveler Application [alpha] {self._name}"

    def __repr__(self):
        return f"{self.__class__.__name__}()"

    def get_by_session_uuid(self, session_uuid: str):
        """Get all messages by session UUID."""

        with self._session as session:

            messages = session.query(Assistance).filter_by(
                session_uuid=session_uuid
            ).order_by(Assistance.created).all()

            return messages
