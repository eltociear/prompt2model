"""An interface for dataset retrieval."""

from __future__ import annotations  # noqa FI58

from abc import ABC, abstractmethod

import datasets

from prompt2model.prompt_parser import PromptSpec


# pylint: disable=too-few-public-methods
class DatasetRetriever(ABC):
    """A class for retrieving datasets."""

    @abstractmethod
    def retrieve_dataset_dict(
        self, prompt_spec: PromptSpec
    ) -> datasets.DatasetDict | None:
        """Retrieve full dataset splits (e.g. train/dev/test) from a prompt.

        Args:
            prompt_spec: A prompt spec (containing a system description).

        Returns:
            A retrieved DatasetDict containing train/val/test splits.
        """
