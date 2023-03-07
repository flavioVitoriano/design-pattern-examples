# borg design pattern
# this design pattern is not a GOF design pattern, it is very similiar to singleton, but with sharing state instead
# of creating a single instance


class Config:
    # this attribute is shared between all Borg instances
    _shared_memory: dict = {}

    def set_attr(self, label: str, value: str):
        self._shared_memory[label] = value

    def get_attr(self, label: str) -> str:
        return self._shared_memory[label]


if __name__ == "__main__":
    config_a = Config()
    config_b = Config()

    config_a.set_attr("global_path", "somepath")

    assert config_b.get_attr("global_path") == "somepath"
    assert config_a is not config_b
