from algopy import ARC4Contract, Bytes, String, Box, arc4
from algopy.arc4 import abimethod


class HelloWorld(ARC4Contract):
    def __init__(self) -> None:
        self.GREETING_BOX = Box(String, key="Greeting")

    @abimethod()
    def hello(self, name: String) -> String:
        greeting = String("Hello ") + name
        self.GREETING_BOX.value = greeting
        return greeting

