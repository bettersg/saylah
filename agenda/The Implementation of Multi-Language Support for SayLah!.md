# The Implementation of Multi-Language Support for SayLah!

## Introduction

As mentioned by the representatives from ISAAC, multi-lingual support was an important feature for AAC applications in Singapore. Most AAC apps have support for only one language, in most cases English. SayLah, at it's current state, is indicative of this issue, although it works for German and French languages in addition to English.

## Reasoning

There are two main reasons why this happens:

|        Reason        |                 English Illiteracy in Users                  |               English Illiteracy in Caregivers               |
| :------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|  **Substantiation**  | Elderly AAC users may face this issue, due to the preexisting language barrier. | Many Caretakers in Singapore speak Mandarin and other local languages. |
|     **Rebuttal**     | In Singapore, children are able to speak English and are familiar with the language. |                              -                               |
| **Feature Required** |                     Tiles require I18N.                      |                Multi-Lingual Text-to-Speech.                 |



## Additional Notes from ISAAC

### Translation Functionalities

Some translation can be employed to do our work (not for the full app, see next note). The possible ways to translate would be:

- [Google Translate API](https://cloud.google.com/translate)
- [The DeepL API](https://www.deepl.com/en/docs-api/)

### Simply Translating is not gonna work.

Verbatim Translation is not the solution to our issue.

Elderly AAC users may also require help, as even IF they speak English, they may need help communicating with their helpers who may not be able to speak English.

We may wish to rely on something similar to [KomunIKON's IKON icon-based language](https://www.komunikon.com/en), with whom we are currently planning to collaborate.