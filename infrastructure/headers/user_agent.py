"""
Modify from https://github.com/joke2k/faker.
"""
import datetime
import random


class UserAgent:
    user_agents = (
        'chrome', 'firefox', 'internet_explorer', 'opera', 'safari',
    )

    windows_platform_tokens = (
        'Windows 95', 'Windows 98', 'Windows 98; Win 9x 4.90', 'Windows CE',
        'Windows NT 4.0', 'Windows NT 5.0', 'Windows NT 5.01',
        'Windows NT 5.1', 'Windows NT 5.2', 'Windows NT 6.0', 'Windows NT 6.1',
        'Windows NT 6.2',
    )

    linux_processors = ('i686', 'x86_64',)

    mac_processors = ('Intel', 'PPC', 'U; Intel', 'U; PPC',)

    def mac_processor(self):
        return random.choice(self.mac_processors)

    def linux_processor(self):
        return random.choice(self.linux_processors)

    def user_agent(self):
        name = random.choice(self.user_agents)
        return getattr(self, name)()

    def common_chrome(self):
        return "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"

    def common_android(self):
        return "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36"

    def android(self):
        phones = (
            "Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36",
            'Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Mobile Safari/537.36'
            'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Mobile Safari/537.36',
        )
        return random.choice(phones)

    def chrome(self, version_from=13, version_to=63,
               build_from=800, build_to=899):
        saf = str(random.randint(531, 536)) + \
            str(random.randint(0, 2))
        tmplt = '({0}) AppleWebKit/{1} (KHTML, like Gecko)' \
                ' Chrome/{2}.0.{3}.0 Safari/{4}'
        platforms = (
            tmplt.format(self.linux_platform_token(),
                         saf,
                         random.randint(version_from, version_to),
                         random.randint(build_from, build_to),
                         saf),
            tmplt.format(self.windows_platform_token(),
                         saf,
                         random.randint(version_from, version_to),
                         random.randint(build_from, build_to),
                         saf),
            tmplt.format(self.mac_platform_token(),
                         saf,
                         random.randint(version_from, version_to),
                         random.randint(build_from, build_to),
                         saf),
        )

        return 'Mozilla/5.0 ' + random.choice(platforms)

    def date_time_between(self, start_date):
        now = datetime.datetime.now()
        now_stamp = int(now.timestamp())
        start_stamp = int(start_date.timestamp())
        random_stamp = random.randint(start_stamp, now_stamp)
        date = datetime.datetime.fromtimestamp(random_stamp)
        return date

    def locale(self):
        language_locale_codes = {
            'aa': ('DJ', 'ER', 'ET'), 'af': ('ZA',), 'ak': ('GH',), 'am': ('ET',),
            'an': ('ES',), 'apn': ('IN',),
            'ar': ('AE', 'BH', 'DJ', 'DZ', 'EG', 'EH', 'ER', 'IL', 'IN',
                   'IQ', 'JO', 'KM', 'KW', 'LB', 'LY', 'MA', 'MR', 'OM',
                   'PS', 'QA', 'SA', 'SD', 'SO', 'SS', 'SY', 'TD', 'TN',
                   'YE'),
            'as': ('IN',), 'ast': ('ES',), 'ayc': ('PE',), 'az': ('AZ', 'IN'),
            'be': ('BY',), 'bem': ('ZM',), 'ber': ('DZ', 'MA'), 'bg': ('BG',),
            'bhb': ('IN',), 'bho': ('IN',), 'bn': ('BD', 'IN'), 'bo': ('CN', 'IN'),
            'br': ('FR',), 'brx': ('IN',), 'bs': ('BA',), 'byn': ('ER',),
            'ca': ('AD', 'ES', 'FR', 'IT'), 'ce': ('RU',), 'ckb': ('IQ',),
            'cmn': ('TW',), 'crh': ('UA',), 'cs': ('CZ',), 'csb': ('PL',),
            'cv': ('RU',), 'cy': ('GB',), 'da': ('DK',),
            'de': ('AT', 'BE', 'CH', 'DE', 'LI', 'LU'), 'doi': ('IN',),
            'dv': ('MV',), 'dz': ('BT',), 'el': ('GR', 'CY'),
            'en': ('AG', 'AU', 'BW', 'CA', 'DK', 'GB', 'HK', 'IE', 'IN', 'NG',
                   'NZ', 'PH', 'SG', 'US', 'ZA', 'ZM', 'ZW'),
            'eo': ('US',),
            'es': ('AR', 'BO', 'CL', 'CO', 'CR', 'CU', 'DO', 'EC', 'ES', 'GT',
                   'HN', 'MX', 'NI', 'PA', 'PE', 'PR', 'PY', 'SV', 'US', 'UY', 'VE'
                   ), 'et': ('EE',), 'eu': ('ES', 'FR'), 'fa': ('IR',),
            'ff': ('SN',), 'fi': ('FI',), 'fil': ('PH',), 'fo': ('FO',),
            'fr': ('CA', 'CH', 'FR', 'LU'), 'fur': ('IT',), 'fy': ('NL', 'DE'),
            'ga': ('IE',), 'gd': ('GB',), 'gez': ('ER', 'ET'), 'gl': ('ES',),
            'gu': ('IN',), 'gv': ('GB',), 'ha': ('NG',), 'hak': ('TW',),
            'he': ('IL',), 'hi': ('IN',), 'hne': ('IN',), 'hr': ('HR',),
            'hsb': ('DE',), 'ht': ('HT',), 'hu': ('HU',), 'hy': ('AM',),
            'ia': ('FR',), 'id': ('ID',), 'ig': ('NG',), 'ik': ('CA',),
            'is': ('IS',), 'it': ('CH', 'IT'), 'iu': ('CA',), 'iw': ('IL',),
            'ja': ('JP',), 'ka': ('GE',), 'kk': ('KZ',), 'kl': ('GL',),
            'km': ('KH',), 'kn': ('IN',), 'ko': ('KR',), 'kok': ('IN',),
            'ks': ('IN',), 'ku': ('TR',), 'kw': ('GB',), 'ky': ('KG',),
            'lb': ('LU',), 'lg': ('UG',), 'li': ('BE', 'NL'), 'lij': ('IT',),
            'ln': ('CD',), 'lo': ('LA',), 'lt': ('LT',), 'lv': ('LV',),
            'lzh': ('TW',), 'mag': ('IN',), 'mai': ('IN',), 'mg': ('MG',),
            'mhr': ('RU',), 'mi': ('NZ',), 'mk': ('MK',), 'ml': ('IN',),
            'mn': ('MN',), 'mni': ('IN',), 'mr': ('IN',), 'ms': ('MY',),
            'mt': ('MT',), 'my': ('MM',), 'nan': ('TW',), 'nb': ('NO',),
            'nds': ('DE', 'NL'), 'ne': ('NP',), 'nhn': ('MX',),
            'niu': ('NU', 'NZ'), 'nl': ('AW', 'BE', 'NL'), 'nn': ('NO',),
            'nr': ('ZA',), 'nso': ('ZA',), 'oc': ('FR',), 'om': ('ET', 'KE'),
            'or': ('IN',), 'os': ('RU',), 'pa': ('IN', 'PK'),
            'pap': ('AN', 'AW', 'CW'), 'pl': ('PL',), 'ps': ('AF',),
            'pt': ('BR', 'PT'), 'quz': ('PE',), 'raj': ('IN',), 'ro': ('RO',),
            'ru': ('RU', 'UA'), 'rw': ('RW',), 'sa': ('IN',), 'sat': ('IN',),
            'sc': ('IT',), 'sd': ('IN', 'PK'), 'se': ('NO',), 'shs': ('CA',),
            'si': ('LK',), 'sid': ('ET',), 'sk': ('SK',), 'sl': ('SI',),
            'so': ('DJ', 'ET', 'KE', 'SO'), 'sq': ('AL', 'ML'), 'sr': ('ME', 'RS'),
            'ss': ('ZA',), 'st': ('ZA',), 'sv': ('FI', 'SE'), 'sw': ('KE', 'TZ'),
            'szl': ('PL',), 'ta': ('IN', 'LK'), 'tcy': ('IN',), 'te': ('IN',),
            'tg': ('TJ',), 'th': ('TH',), 'the': ('NP',), 'ti': ('ER', 'ET'),
            'tig': ('ER',), 'tk': ('TM',), 'tl': ('PH',), 'tn': ('ZA',),
            'tr': ('CY', 'TR'), 'ts': ('ZA',), 'tt': ('RU',), 'ug': ('CN',),
            'uk': ('UA',), 'unm': ('US',), 'ur': ('IN', 'PK'), 'uz': ('UZ',),
            've': ('ZA',), 'vi': ('VN',), 'wa': ('BE',), 'wae': ('CH',),
            'wal': ('ET',), 'wo': ('SN',), 'xh': ('ZA',), 'yi': ('US',),
            'yo': ('NG',), 'yue': ('HK',), 'zh': ('CN', 'HK', 'SG', 'TW'),
            'zu': ('ZA',)
        }
        language_code = random.choice([i for i in language_locale_codes.keys()])
        loc = random.choice(language_locale_codes[language_code])
        return language_code + '-' + loc

    def firefox(self):
        ver = (
            'Gecko/{0} Firefox/{1}.0'.format(
                self.date_time_between(
                    datetime.datetime(2011, 1, 1)
                ).date(),
                random.randint(4, 15)
            ).replace('-', ''),
            'Gecko/{0} Firefox/3.6.{1}'.format(
                self.date_time_between(
                    datetime.datetime(2010, 1, 1)
                ).date(),
                random.randint(1, 20)
            ).replace('-', ''),
            'Gecko/{0} Firefox/3.8'.format(
                self.date_time_between(
                    datetime.datetime(2010, 1, 1)
                ).date(),
            ).replace('-', ''),
        )
        tmplt_win = '({0}; {1}; rv:1.9.{2}.20) {3}'
        tmplt_lin = '({0}; rv:1.9.{1}.20) {2}'
        tmplt_mac = '({0}; rv:1.9.{1}.20) {2}'
        platforms = (
            tmplt_win.format(self.windows_platform_token(),
                             self.locale(),
                             random.randint(0, 2),
                             random.choice(ver)),
            tmplt_lin.format(self.linux_platform_token(),
                             random.randint(5, 7),
                             random.choice(ver)),
            tmplt_mac.format(self.mac_platform_token(),
                             random.randint(2, 6),
                             random.choice(ver)),
        )

        return 'Mozilla/5.0 ' + random.choice(platforms)

    def safari(self):
        saf = "{0}.{1}.{2}".format(random.randint(531, 535),
                                   random.randint(1, 50),
                                   random.randint(1, 7))
        if not random.getrandbits(1):
            ver = "{0}.{1}".format(random.randint(4, 5),
                                   random.randint(0, 1))
        else:
            ver = "{0}.0.{1}".format(random.randint(4, 5),
                                     random.randint(1, 5))
        tmplt_win = '(Windows; U; {0}) AppleWebKit/{1} (KHTML, like Gecko)' \
                    ' Version/{2} Safari/{3}'
        tmplt_mac = '({0} rv:{1}.0; {2}) AppleWebKit/{3} (KHTML, like Gecko)' \
                    ' Version/{4} Safari/{5}'
        tmplt_ipod = '(iPod; U; CPU iPhone OS {0}_{1} like Mac OS X; {2})' \
                     ' AppleWebKit/{3} (KHTML, like Gecko) Version/{4}.0.5' \
                     ' Mobile/8B{5} Safari/6{6}'
        locale = self.locale()
        platforms = (
            tmplt_win.format(self.windows_platform_token(),
                             saf,
                             ver,
                             saf),
            tmplt_mac.format(self.mac_platform_token(),
                             random.randint(2, 6),
                             locale,
                             saf,
                             ver,
                             saf),
            tmplt_ipod.format(random.randint(3, 4),
                              random.randint(0, 3),
                              locale,
                              saf,
                              random.randint(3, 4),
                              random.randint(111, 119),
                              saf),
        )

        return 'Mozilla/5.0 ' + random.choice(platforms)

    def opera(self):
        platform = '({0}; {1}) Presto/2.9.{2} Version/{3}.00'.format(
            (
                self.linux_platform_token()
                if random.getrandbits(1)
                else self.windows_platform_token()
            ),
            self.locale(),
            random.randint(160, 190),
            random.randint(10, 12),
        )
        return 'Opera/{0}.{1}.{2}'.format(
            random.randint(8, 9),
            random.randint(10, 99),
            platform,
        )

    def internet_explorer(self):
        tmplt = 'Mozilla/5.0 (compatible; MSIE {0}.0; {1}; Trident/{2}.{3})'
        return tmplt.format(random.randint(5, 9),
                            self.windows_platform_token(),
                            random.randint(3, 5),
                            random.randint(0, 1))

    def windows_platform_token(self):
        return random.choice(self.windows_platform_tokens)

    def linux_platform_token(self):
        return 'X11; Linux {0}'.format(
            random.choice(self.linux_processors))

    def mac_platform_token(self):
        return 'Macintosh; {0} Mac OS X 10_{1}_{2}'.format(
            random.choice(self.mac_processors),
            random.randint(5, 12),
            random.randint(0, 9),
        )


if __name__ == '__main__':
    ua = UserAgent()
    headers = getattr(ua, 'common_android')
    print(headers)
