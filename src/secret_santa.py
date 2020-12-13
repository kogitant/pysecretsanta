import random
import sys
import time

import typing


class SecretSantaResults:
    pairs: typing.Dict[str, str] = {}

    def __init__(self, people: typing.List[str]) -> None:
        super().__init__()
        self.people = people

    def gifters(self) -> typing.List[str]:
        return self.pairs.keys()

    def get_recipient_of_gifter(self, name: str) -> str:
        return self.pairs.get(name)

    def recipients(self) -> typing.List[str]:
        return self.pairs.values()

    def add(self, gifter: str, recipient: str):
        self.pairs[gifter] = recipient

    def evensteven(self) -> bool:
        return len(self.pairs) > 0 and len(self.pairs) == len(self.people)

    def reset(self):
        self.pairs.clear()

    def people_left_for_gifting(self):
        candidates: typing.List[str] = self.people.copy()
        for name in self.recipients():
            candidates.remove(name)
        return candidates


class SecretSanta:
    names: typing.List[str] = []
    results: SecretSantaResults = None

    def __init__(self, names: typing.List[str]) -> None:
        super().__init__()
        self.names = names
        self.results = SecretSantaResults(people=names)

    def select_recipient_for(self, gifter: str):
        candidates = self.results.people_left_for_gifting()

        if gifter in candidates:
            candidates.remove(gifter)
        selected = gifter

        # Seems that the gifter would need to give a gift to themselves
        # This special scenario requires altering the already drawn pairings
        if len(candidates) == 0:
            last_pair: typing.Tuple[str, str] = self.results.pairs.popitem()
            self.results.add(last_pair[0], gifter)
            return last_pair[1]
        elif len(candidates) == 1:
            # Only one recipient to choose from, returning them
            return candidates[0]

        draw_attempt = 0
        while selected == gifter:
            draw_attempt += 1
            r = random.randrange(0, len(candidates))
            selected = candidates[r]

        return selected

    def draw_gifters_and_recipients(self) -> SecretSantaResults:
        while not self.results.evensteven():
            self.results.reset()
            for gifter in self.names:
                recipient = self.select_recipient_for(gifter)
                self.results.add(gifter, recipient)

        return self.results

    def perform(self, lang: str):
        results = self.draw_gifters_and_recipients()
        for gifter, recipient in self.results.pairs.items():
            r = random.randrange(25, 75)
            sys.stdout.write(self.drawing_text(lang, gifter))
            for i in range(0, r):
                sys.stdout.write(".")
                sys.stdout.flush()
                time.sleep(0.1)
            print(
                "\n\t"
                + self.recipient_for_gifter_selected_text(gifter, recipient, lang)
            )

    def drawing_text(self, lang: str, gifter: str):
        if lang and lang == "fi":
            return "Kun arvontalaulu raikaa, on aaarvonnan aaaikaaa. Kelle nalli napsahtaa {}, kelle nalli napsahtaa?".format(
                gifter
            )
        else:
            return "Drawing recipient for {}".format(gifter)

    def recipient_for_gifter_selected_text(self, gifter, recipient, lang):
        if lang and lang == "fi":
            return "{} antoopi lahjan henkilölle {}".format(gifter, recipient)
        else:
            return "{} gives a gift to {}".format(gifter, recipient)
