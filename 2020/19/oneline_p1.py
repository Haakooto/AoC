import re

print(sum((rules := {int(num): rest for num, rest in [rule.split(": ") for rule in open("inputs19").read().strip().split("\n\n")[0].splitlines()]}, regexes := {}, [bool(re.fullmatch(regex0 := (get_regex := (lambda num: regexes[num] if num in regexes else (regexes.__setitem__(num, regex := ("(" + ")|(".join(["(" + ")(".join([get_regex(int(i)) for i in option.split(" ")]) + ")" for option in rules[num].split(" | ")]) + ")") if rules[num] not in ("a",  "b") else rules[num]), regex)[1]))(0), msg)) for msg in open("inputs19").read().strip().split("\n\n")[1].splitlines()])[2]))
# while line 3 above, which in a single line finds and prints answer to part 1 of AoC 2020 day 19, is horrible and must not be attempted to be understood in other ways than looking at the file monster_messages_1.py, which is the outwritten form of it, or viewing the comment below which is the result of PEP8-ed formatting of it through 'black', it is curious to note that this very comment it is a single-sentaced text containing the information wish to convey through this comment and should be seen as no less acomplisment, this aggrevated by the fact that they share length.
"""
print(
    sum(
        (
            rules := {
                int(num): rest
                for num, rest in [
                    rule.split(": ")
                    for rule in open("inputs19")
                    .read()
                    .strip()
                    .split("\n\n")[0]
                    .splitlines()
                ]
            },
            regexes := {},
            [
                bool(
                    re.fullmatch(
                        regex0 := (
                            get_regex := (
                                lambda num: regexes[num]
                                if num in regexes
                                else (
                                    regexes.__setitem__(
                                        num,
                                        regex := (
                                            "("
                                            + ")|(".join(
                                                [
                                                    "("
                                                    + ")(".join(
                                                        [
                                                            get_regex(int(i))
                                                            for i in option.split(" ")
                                                        ]
                                                    )
                                                    + ")"
                                                    for option in rules[num].split(
                                                        " | "
                                                    )
                                                ]
                                            )
                                            + ")"
                                        )
                                        if rules[num] not in ("a", "b")
                                        else rules[num],
                                    ),
                                    regex,
                                )[1]
                            )
                        )(0),
                        msg,
                    )
                )
                for msg in open("inputs19").read().strip().split("\n\n")[1].splitlines()
            ],
        )[2]
    )
)
"""
