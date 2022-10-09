class DescriptorClass:
    def __get__(self, instance, owner):
        if instance is None:
            print("Instance is none")
            return f"{self.__class__.__name__}.{owner.__name__}"
        return f"value for {instance}"


class ClientClass:
    descriptor = DescriptorClass()


if __name__ == "__main__":
    print(ClientClass.descriptor)
    client_object = ClientClass()
    print(client_object.descriptor)
