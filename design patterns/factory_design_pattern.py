###################################################################################################################################################

'''
Factory Method is a creational design pattern used to create concrete implementations of a common interface.

It separates the process of creating an object from the code that depends on the interface of the object.

For example, an application requires an object with a specific interface to perform its tasks. The concrete implementation of the interface is
identified by some parameter.

Instead of using a complex if/elif/else conditional structure to determine the concrete implementation, the application delegates that 
decision to a separate component that creates the concrete object. With this approach, the application code is simplified, making 
it more reusable and easier to maintain.

Imagine an application that needs to convert a Song object into its string representation using a specified format. Converting an
object to a different representation is often called serializing. You'll often see these requirements implemented in a single function
or method that contains all the logic and implementation, like in the following code:


########### The Problems With Complex Conditional Code

The example above exhibits all the problems you'll find in complex logical code. Complex logical code uses if/elif/else structures to 
change the behavior of an application. Using if/elif/else conditional structures makes the code harder to read, harder to understand, 
and harder to maintain.

The code above might not seem hard to read or understand, but wait till you see the final code in this section!

Nevertheless, the code above is hard to maintain because it is doing too much. The single responsibility principle states that a module, 
a class, or even a method should have a single, well-defined responsibility. It should do just one thing and have only one reason to change.

The .serialize() method in SongSerializer will require changes for many different reasons. This increases the risk of introducing 
new defects or breaking existing functionality when changes are made. Let's take a look at all the situations that will require modifications 
to the implementation:

When a new format is introduced: The method will have to change to implement the serialization to that format.

When the Song object changes: Adding or removing properties to the Song class will require the implementation to change in order to 
accommodate the new structure.

When the string representation for a format changes (plain JSON vs JSON API): The .serialize() method will have to change if 
the desired string representation for a format changes because the representation is hard-coded in the .serialize() method implementation.

'''


###################################################################################################################################################
##################### Example 1 #####################

# Without Factory Design Pattern

class FrenchLocalizer:
    def __init__(self):
        self.translations = {
            "car": "voiture", 
            "bike": "bicyclette",
            "cycle":"cyclette"
        }
 
    def localize(self, msg):
        return self.translations.get(msg, msg)
 
class SpanishLocalizer:
    def __init__(self):
        self.translations = {
            "car": "coche", 
            "bike": "bicicleta",
            "cycle":"ciclo"
        }
 
    def localize(self, msg):
        return self.translations.get(msg, msg)
 
class EnglishLocalizer:
    def localize(self, msg):
        return msg

# Use these classes
if __name__ == "__main__":
 
    f = FrenchLocalizer()
    e = EnglishLocalizer()
    s = SpanishLocalizer()
 
    message = ["car", "bike", "cycle"]
 
    for msg in message:
        print(f.localize(msg))
        print(e.localize(msg))
        print(s.localize(msg))

# With Factory Desgin

class FrenchLocalizer:
	def __init__(self):
		self.translations = {
            "car": "voiture", 
            "bike": "bicyclette",
			"cycle":"cyclette"
        }

	def localize(self, msg):
		return self.translations.get(msg, msg)

class SpanishLocalizer:
	def __init__(self):
		self.translations = {
            "car": "coche", 
            "bike": "bicicleta",
			"cycle":"ciclo"
        }

	def localize(self, msg):
		return self.translations.get(msg, msg)

class EnglishLocalizer:
	def localize(self, msg):
		return msg

def Factory(language ="English"):
	localizers = {
		"French": FrenchLocalizer,
		"English": EnglishLocalizer,
		"Spanish": SpanishLocalizer,
	}
	return localizers[language]()

if __name__ == "__main__":

	f = Factory("French")
	e = Factory("English")
	s = Factory("Spanish")
        
	message = ["car", "bike", "cycle"]

	for msg in message:
		print(f.localize(msg))
		print(e.localize(msg))
		print(s.localize(msg))


###################################################################################################################################################
##################### Example 2 #####################
import json
import xml.etree.ElementTree as et

# Without Factory Design Pattern

class Song:
    def ___init__(self, id: int, title: str, artist: str):
        self.id = id
        self.title = title
        self.artist = artist

class SongSerializer:
    def serialize(self, song: Song, format: str=None):
        if format == "json":
            json_song = {
                "id": song.id,
                "title": song.title,
                "artist": song.artist
            }
            return json.dumps(json_song)
        elif format == "xml":
            xml_song = et.Element('song', attrib={"id": song.id})
            title = et.SubElement(xml_song, "title")
            title.text = song.title
            artist = et.SubElement(xml_song, 'artist')
            artist.text = song.artist
            return et.tostring(xml_song, encoding="unicode")
        else:
            raise Exception("Format not implement yet!")

# With Factory Design Pattern but without Reusability

class SongSerializer:
    def serialize(self, song: Song, format: str=None):
        serializer = self._get_serializer(format)
        return serializer(song)

    def _get_serializer(self, format: str=None):
        if format == "json":
            return self._serialize_to_json
        elif format == "xml":
            return self._serialize_to_xml
        else:
            raise Exception("Format not implement yet!")
        
    def _serialize_to_json(self, song: Song):
        json_song = {
            "id": song.id,
            "title": song.title,
            "artist": song.artist
        }
        return json.dumps(json_song)

    def _serialize_to_xml(self, song: Song):
        xml_song = et.Element('song', attrib={"id": song.id})
        title = et.SubElement(xml_song, "title")
        title.text = song.title
        artist = et.SubElement(xml_song, 'artist')
        artist.text = song.artist
        return et.tostring(xml_song, encoding="unicode")


# With Factory Design Pattern but with Reusability

# Now these methods is independent to class and can be use anywhere
def get_serializer(format: str=None):
    if format == "json":
        return serialize_to_json
    elif format == "xml":
        return serialize_to_xml
    else:
        raise Exception("Format not implement yet!")

def serialize_to_json(song: Song):
    json_song = {
        "id": song.id,
        "title": song.title,
        "artist": song.artist
    }
    return json.dumps(json_song)

def serialize_to_xml(song: Song):
    xml_song = et.Element('song', attrib={"id": song.id})
    title = et.SubElement(xml_song, "title")
    title.text = song.title
    artist = et.SubElement(xml_song, 'artist')
    artist.text = song.artist
    return et.tostring(xml_song, encoding="unicode")

class SongSerializer:
    def serialize(self, song: Song, format: str=None):
        serializer = get_serializer(format)
        return serializer(song)



'''
########
Advantages of using Factory method: 
#######
We can easily add new types of products without disturbing the existing client code.
Generally, tight coupling is being avoided between the products and the creator classes and objects.

#############
Disadvantages of using Factory method:
############
To create a particular concrete product object, the client might have to sub-class the creator class.

You end up with a huge number of small files i.e, cluttering the files.

In a Graphics system, depending upon the user's input it can draw different shapes like rectangles, Square, Circle, etc. But for the ease of both 
developers as well as the client, we can use the factory method to create the instance depending upon the user's input. Then we don't have to 
change the client code for adding a new shape.

On a Hotel booking site, we can book a slot for 1 room, 2 rooms, 3 rooms, etc. Here user can input the number of rooms he wants to book. 
Using the factory method, we can create a factory class Any Rooms which will help us to create the instance depending upon the user's input. 
Again we don't have to change the client's code for adding the new facility.

'''