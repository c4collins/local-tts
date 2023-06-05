# Local TTS for Windows (and beyond?)

## Usage

### TTS:

```
main.exe --message "Hello" --voice 0 --rate 150
```

All values are optional

- Default `--message` is: Hello, World!
- Default `--rate` is: 145
- Default `--voice` is: 1

### Finding Voices

This program should pick up on any local TTS voices that you have installed.

```
main.exe --voices --rate 300
```
This will have every TTS voice on your system read you their name and number.
It's a bit slow and can't be interrupted, so I tend to run this with a `--rate` of 300 or higher (I have like 16 voices installed locally)

Check the next section for installing new voices.

## Installing Voices

In the repository (https://github.com/c4collins/local-tts.git) there's a folder called `/voices` containing some `.reg` files.
Each of those files contains a registry instruction that will add a different voice to your system.

Doing registry edits is something I didn't want to include in the main application, but the voice files are there if you want to use them.

They're just text descriptions of registry keys, you can open them in any text editing program.


e.g.:
```
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-CA_LINDA_11.0]
@="Microsoft Linda - English (Canada)"
"1009"="Microsoft Linda - English (Canada)"
"CLSID"="{179F3D56-1B0B-42B2-A962-59B7EF59FE1B}"
"LangDataPath"=hex(2):25,00,77,00,69,00,6e,00,64,00,69,00,72,00,25,00,5c,00,53,\
  00,70,00,65,00,65,00,63,00,68,00,5f,00,4f,00,6e,00,65,00,43,00,6f,00,72,00,\
  65,00,5c,00,45,00,6e,00,67,00,69,00,6e,00,65,00,73,00,5c,00,54,00,54,00,53,\
  00,5c,00,65,00,6e,00,2d,00,43,00,41,00,5c,00,4d,00,53,00,54,00,54,00,53,00,\
  4c,00,6f,00,63,00,65,00,6e,00,43,00,41,00,2e,00,64,00,61,00,74,00,00,00
"VoicePath"=hex(2):25,00,77,00,69,00,6e,00,64,00,69,00,72,00,25,00,5c,00,53,00,\
  70,00,65,00,65,00,63,00,68,00,5f,00,4f,00,6e,00,65,00,43,00,6f,00,72,00,65,\
  00,5c,00,45,00,6e,00,67,00,69,00,6e,00,65,00,73,00,5c,00,54,00,54,00,53,00,\
  5c,00,65,00,6e,00,2d,00,43,00,41,00,5c,00,4d,00,34,00,31,00,30,00,35,00,4c,\
  00,69,00,6e,00,64,00,61,00,00,00

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-CA_LINDA_11.0\Attributes]
"Age"="Adult"
"DataVersion"="11.0.2015.0909"
"Gender"="Female"
"Language"="1009"
"Name"="Microsoft Linda"
"SayAsSupport"="spell=NativeSupported; cardinal=NativeSupported; ordinal=NativeSupported; date=NativeSupported; time=NativeSupported; address=NativeSupported; telephone=NativeSupported; computer=NativeSupported; currency=NativeSupported; message=NativeSupported; name=NativeSupported; media=NativeSupported; url=NativeSupported; alphanumeric=NativeSupported"
"SharedPronunciation"=""
"Vendor"="Microsoft"
"Version"="11.0"
```

## Notes

I don't offer support for any of my software; this is strictly at your own risk, but I will guarantee that it's free of malicious intent.
