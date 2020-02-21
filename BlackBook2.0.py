# This example show how to use inline keyboards and process button presses
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, MessageEntity

TELEGRAM_TOKEN = '854878569:AAFxsphCoXRPxLGRCrUW3x9tA98KXqyK-00'

bot = telebot.TeleBot('1098940256:AAHDRseehNUEDQ1neeT3E-2b5-6BzxIMZ8A')
teachers = \
{
	"кі" : \
	{
		"1" : \
		{
		    	"none" : \
			{
				"Англ" : \
                                {
                                    "Ажогіна Н.В."      : "https://docs.google.com/forms/d/e/1FAIpQLScZepnZtA84rIJzJg-z07mwySTJL977LwLxJF_KPtnQ207smA/viewform",
                                    "Александрук І.В."  : "https://docs.google.com/forms/d/e/1FAIpQLSfl13HzDcKkW6Btks_cdOpwThtDQKUbK0S4zyDrrYsgMtriug/viewform",
                                    "Гонта І.А."        : "https://docs.google.com/forms/d/e/1FAIpQLSeZon8ElAeZAyJIXyPMlPTmSa8zrocsBtFi9MvXIwlAbuEvCw/viewform",
                                    "Кирилюк О.Л."      : "https://docs.google.com/forms/d/e/1FAIpQLSetJ0zMKSLIv_AUsBpsPpTEUAkiHwBVPtic7t74wSZzeVKtmA/viewform",
                                    "Титова О.І."       : "https://docs.google.com/forms/d/e/1FAIpQLSdJpZ5g1w9m69FqrSxFuaubUUMoo0r3xRMIPj_MYV7VvfWjzQ/viewform",
                                    "Янчук С.Я."        : "https://docs.google.com/forms/d/e/1FAIpQLSfOyP5hETLzM8h6vImzyKvxP-BZhlykON-7QOrNaEHNnOIh1w/viewform"
                                },
                                "ОАПЗ" : \
                                
                                    {
                                        "Бойко Ю.В."            : "https://docs.google.com/forms/d/e/1FAIpQLSfB86GE5pZjiIFy1o-4vktYut0z_lw1EFXqjDkfrqYVnXcEtw/viewform",
                                        "Борецький О.Ф."        : "https://docs.google.com/forms/d/e/1FAIpQLSfEHRwSehN9JWD_kv0_qyQqck8Qg8bHWPEGQnG_BJXFTXOshQ/viewform",
                                        "Зарембовський К.В."    : "https://docs.google.com/forms/d/e/1FAIpQLScJmgugFGXxGhaTWs7n4BDCB3C1Sz-b-TmhkDCG9hF1cEqHOQ/viewform"
                                    },
                                "Фізика" : \
                                
                                    {
                                        "Висоцький М.В."    : "https://docs.google.com/forms/d/e/1FAIpQLSewq5mYsjYOds3OVF7pE3ZEPgvoaOv7gRdedZxDLD7oonTNxw/viewform",
                                        "Короновський В.Є." : "https://docs.google.com/forms/d/e/1FAIpQLSeqE0jFV5KZrgDTBPxSLYs-2HvGo_ANlJbD1klgypqsspx8Jg/viewform",
                                        "Сохацький В.П."    : "https://docs.google.com/forms/d/e/1FAIpQLSfWp9IpWMoqJaKpKlHzoM1_qZ-Ao-LtPKm3LUckThTBJw809A/viewform"
                                    },
                                "Вишмат" : \
                                
                                    {
                                        "Єфіменко С.В."     : "https://docs.google.com/forms/d/e/1FAIpQLSc3uIDJ56l61ZkICCVhoG6XnOKyXazl_fEkV23WI0PXkfenRw/viewform",
                                        "Іваненко Д.О."     : "https://docs.google.com/forms/d/e/1FAIpQLSep2Y6j9HA30aI2fa-yqQQzKX2Cuz-J2svFA88KhR_V5FN11g/viewform",
                                        "Львов А.В."        : "https://docs.google.com/forms/d/e/1FAIpQLSecfSM48rPvA439_LauekyRcX33Is6_s08R8RYvak0MVIVKUg/viewform",
                                        "Моторна О.В."      : "https://docs.google.com/forms/d/e/1FAIpQLSekzzZPVVFe0m9I05nwyqjEG4KR_Q9ekLzFEjiGTSZSQKmIfg/viewform",
                                        "Радченко О.М."     : "https://docs.google.com/forms/d/e/1FAIpQLSfkmyNdCHMgjVxMplM6XCIxKThif0MPl3dbVgbHhlq2d5kpDA/viewform",
                                        "Ральченко С.А."    : "https://docs.google.com/forms/d/e/1FAIpQLSfff5nr5Ru1kLVb2tyF1EsMdUFkZbLpH_p2dr3eWwpsRPlnag/viewform",
                                        "" : ""
                                    },
                                "ВДУС" : \
                                
                                    {
                                        "Набока С.В." : "https://docs.google.com/forms/d/e/1FAIpQLSfaBJ73FiTCQ2fX6kZZkmwKkTEdVbwwb6EOvASjBDCweIlEdw/viewform"
                                    },
                                "Програмування" : \
                                
                                    {
                                        "Стрільчук Г.М." : "https://docs.google.com/forms/d/e/1FAIpQLSdq1uwsoHSSfLmQhGrENQoXH_SsFowsnnKBBFEwfelvAuM3dA/viewform"
                                    },
                                
			},
		},
		"2" : \
		{
		    	"none" : \
			{
				"КомпЕл" : \
                                
                                    {
                                        "Бех І.І."      : "https://docs.google.com/forms/d/e/1FAIpQLSfDPaxyzqcu1gOKft_f9WVFAkLgBOmzf7PQGugw435ctnQpLg/viewform",
                                        "Котов М.М."    : "https://docs.google.com/forms/d/e/1FAIpQLScA1deZ-s4KukfYyge5aRxEHo2mbFjwJYmPpMNch4q-aKfqHQ/viewform",
                                        "Фесенко С.А."  : "https://docs.google.com/forms/d/e/1FAIpQLScSGFrBmG3IRVc4kBfEX6ZDSDm-5zEXWXwjHEBr5KB4lfv8PQ/viewform"
                                    },
                                "Філософія" : \
                                
                                    {
                                        "Руденко М.В."      : "https://docs.google.com/forms/d/e/1FAIpQLSeASaLmkFU4QNCm7MoVcTz2JZMTsHQ44mAxwdiXSzeeTFNCiw/viewform",
                                        "Коперльос Р.Ю."    : "https://docs.google.com/forms/d/e/1FAIpQLSeyVBcopnt5UWzdRZwdBcYtEa2VbaQI4kGc4BBkmfH06RIU1Q/viewform",
                                        "Загороднюк В.В."   : "https://docs.google.com/forms/d/e/1FAIpQLScMMbw8YpFfDysaw30XukWU8GaCa-WTNIzir7oMJLpAQIJ4Iw/viewform"
                                    },
                                "Диск" : \
                                
                                    {
                                        "Погорілий С.Д."        : "https://docs.google.com/forms/d/e/1FAIpQLSfVfAiSfKVvdd6VGV6tbZ3A7Z9B4q16KQSxy7tOvgDXcDQBdw/viewform",
                                        "Зарембовський К.В."    : "https://docs.google.com/forms/d/e/1FAIpQLSdg6Q-RJEUsDPH8wvKZJVNoLdJFJLx44M7YYDaz1tMdIeZjkw/viewform"
                                    },
                                "ТЕМ" : \
                                
                                    {
                                        "Мартиш Є.В." : "https://docs.google.com/forms/d/e/1FAIpQLScl6z3dzLjJECdaUAlyYTzea9M9L6JF8Jk3bCQEJrvWiygSWw/viewform"
                                    },
                                "Дифур" : \
                                
                                    {
                                        "Львов В.А." : "https://docs.google.com/forms/d/e/1FAIpQLSd6HJY746jeFoEC73CxZtAO7mwoMFQq9feQPmvoOuM20iHOjQ/viewform"
                                    },
                                "ССМ" : \
                                
                                    {
                                        "Коновалов А.М." : "https://docs.google.com/forms/d/e/1FAIpQLScF8Qine8OdXN6cUj79-b0oxv7bcqZqoJ2DZm3PADUuPTXb0g/viewform"
                                    },
                                
			},
		},
		"3" : \
		{
		    	"ма" : \
			{
				"ІПЗ" : \
                                
                                    {
                                        "Сусь Б.Б." : "https://docs.google.com/forms/d/e/1FAIpQLScZaLEpsMYCD56LPcLUpF84WHlvC36BEhlqJ8E0IeKuTDng0Q/viewform"
                                    },
                                "БД" : \
                                
                                    {
                                        "Слюсар Є.А." : "https://docs.google.com/forms/d/e/1FAIpQLSc1GkccF_ZOs0tfadp7iAiSODdzP0POvC8OEiEAIxOoImkZxg/viewform"
                                    },
                                "Оптел" : \
                                
                                    {
                                        "Первак Ю.О." : "https://docs.google.com/forms/d/e/1FAIpQLSf07rH9ewa1jzr8OwsUGyyAmcOpKqtAD4PkAbvHfsRdj851wA/viewform",
                                        "Внучко С.М." : "https://docs.google.com/forms/d/e/1FAIpQLSdsARzdJWY1hUGjfYwQtuS6bCdJFCOw7I3R2jzoP-F98sGI6w/viewform"
                                    },
                                "Культура" : \
                                
                                    {
                                        "Мураткіна Т.М." : "https://docs.google.com/forms/d/e/1FAIpQLSetThLG80vRD4dut-T5S_ZLGYSkdWmHkbx08O18Ciwj3neFbg/viewform",
                                        "Вдовиченко Г.В." : "https://docs.google.com/forms/d/e/1FAIpQLSdIpHNwm9xu9KbQp9SRjDdDHTpQBwmuMip3d-ePUfa7EtnYmQ/viewform"
                                    },
                                "КомпМер" : \
                                
                                    {
                                        "Мар'яновський В.А." : "https://docs.google.com/forms/d/e/1FAIpQLSdtf-ZELme8UHve4RjcoZ_aMSBDrW0A5fU47N7NlSheYUWrIQ/viewform"
                                    },
                                "СПЗ" : \
                                
                                    {
                                        "Загороднюк С.П." : "https://docs.google.com/forms/d/e/1FAIpQLScv4ZHvWzkSxYN8TOPH1fr79z9CdFQn8NqDhh_3F3fceF6_Kg/viewform"
                                    },
                                "СоцполСт" : \
                                
                                    {
                                        "Внучко С.М." : "https://docs.google.com/forms/d/e/1FAIpQLScpUBpCJLD0N0ZkNHPnAXpM-H59ZC6zuvv_BPl5Lg48sZEjBg/viewform"
                                    }
                                
			},
                        "са" : \
			{
				"ІПЗ" : \
                                
                                    {
                                        "Сусь Б.Б." : "https://docs.google.com/forms/d/e/1FAIpQLSdWTv_Xw3oD45FhU7XlfXcQ5M2H-22LZEpIv23NoXAcLEZKUw/viewform"
                                    },
                                "Оптел" : \
                                
                                    {
                                        "Первак Ю.О." : "https://docs.google.com/forms/d/e/1FAIpQLSd7FEpmXgcatfoxPK9KtXhkOKRaH-Ajr1elqtLfCxFZi4k3bA/viewform",
                                        "Внучко С.М." : "https://docs.google.com/forms/d/e/1FAIpQLSdsARzdJWY1hUGjfYwQtuS6bCdJFCOw7I3R2jzoP-F98sGI6w/viewform"
                                    },
                                "СКБД" : \
                                
                                    {
                                        "Ольшевський С.В." : "https://docs.google.com/forms/d/e/1FAIpQLSfVsqp3k-cYOzhyOBHFi74PG30v4FqUZuBi2VRWeZ5l4jMTIQ/viewform"
                                    },
                                "Культура" : \
                                
                                    {
                                        "Мураткіна Т.М." : "https://docs.google.com/forms/d/e/1FAIpQLSe7OVoTTErVcpyM2Dx3eDOKOKmI_KBisvlrjUkw-Iy-JGb8Jw/viewform",
                                        "Вдовиченко Г.В." : "https://docs.google.com/forms/d/e/1FAIpQLSdgRRumeaMWTTN6_0o9B975iuub9eOHAc7SW9vhqwlFxrb1PA/viewform"
                                    },
                                "КомпМер" : \
                                
                                    {
                                        "Мар'яновський В.А." : "https://docs.google.com/forms/d/e/1FAIpQLScuELe4YnLYv8EonU1Xk1RMHXAY__u--3ae-u-y-Z_d9z83Jw/viewform"
                                    },
                                "СПЗ" : \
                                
                                    {
                                        "Загороднюк С.П." : "https://docs.google.com/forms/d/e/1FAIpQLScOcC4Kni-7OZwQCisS8TPMS0yOEP-i9iuxzvmI7yX8M6im8w/viewform"
                                    },
                                "СоцполСт" : \
                                
                                    {
                                        "Внучко С.М." : "https://docs.google.com/forms/d/e/1FAIpQLSesNS7yx7ocw_TYdyTTVm5csGXFxsXJzKLO8rIm_3MhKZvp8g/viewform"
                                    }
                                
			}
		},
		"4" : \
		{
		    	"ма" : \
			{
				"ОТТ" : \
                                
                                    {
                                        "Слюсар Є.А." : "https://docs.google.com/forms/d/e/1FAIpQLSczG1xI-jlXhv1E1jEw6tQr2-NHoOoAKhdIAhdDZBXdCTrJ8g/viewform"
                                    },
                                "ІС" : \
                                
                                    {
                                        "Сальніков А.О." : "https://docs.google.com/forms/d/e/1FAIpQLSeAgXtGDYc3l--rgW0iOSPgKAd-ERY50eTHz2ztf3wdfvEXGg/viewform"
                                    },
                                "ЗІКС" : \
                                
                                    {
                                        "Сальніков А.О." : "https://docs.google.com/forms/d/e/1FAIpQLSeEcY3YU1iGOuN57B16yrRnaMHM9JilP3m6sC3JdXn3YnrjRg/viewform"
                                    },
                                "ІГ" : \
                                
                                    {
                                        "Нетреба А.В." : "https://docs.google.com/forms/d/e/1FAIpQLSf1AFtFXPpoZg4HG17dKH23QIcQzJT-rvT4rpZsSl3E80-7Og/viewform"
                                    },
                                "ПРО" : \
                                
                                    {
                                        "Борецький О.Ф." : "https://docs.google.com/forms/d/e/1FAIpQLSc9rr6vVPb7DIRkgTK_EhaKTcrgvkfpFjJ5sApl_gkb7hnUIA/viewform"
                                    },
                                "КЛ" : \
                                
                                    {
                                        "Баужа О.С." : "https://docs.google.com/forms/d/e/1FAIpQLSetEalnaCFJE7mak1yNS4UovgHtJJFF3gSCUfB9ARhB5AV2yw/viewform"
                                    },
                                "ЦОС" : \
                                
                                    {
                                        "Барабанов А.В." : "https://docs.google.com/forms/d/e/1FAIpQLSdFXNneHApc2eBbQcsnsok6BXfb6vwT_bxd9bOCKiFBCRJ-gQ/viewform"
                                    },
                                "ТПКС" : \
                                
                                    {
                                        "Барабанов А.В." : "https://docs.google.com/forms/d/e/1FAIpQLSciXCiGXIxtzeJJGWm1gBV-mWZk8wcFQOK8SosRS_f7ftmvOw/viewform"
                                    },
                                "Англ" : \
                                
                                    {
                                        "Александрук І.В." : "https://docs.google.com/forms/d/e/1FAIpQLSdnzh66QYcrkreDD5MmB0chTL2E2fYnyFCHSqGTfqU2f_K3Rg/viewform"
                                    },
			},
                        "са" : \
			{
                                "ЗІКС" : \
                                
                                    {
                                        "Сальніков А.О." : "https://docs.google.com/forms/d/e/1FAIpQLSezitX8qvTPDgpCOjHCwylao_pnBKwlI-9aDkhYWKgLdgE4WQ/viewform"
                                    },
                                "ІГ" : \
                                
                                    {
                                        "Нетреба А.В." : "https://docs.google.com/forms/d/e/1FAIpQLSeOq0UldK5izAqosFPgfxVZ9wk82fwu2fR8Wn-DgmP4nQ3MOQ/viewform"
                                    },
                                "ФП" : \
                                
                                    {
                                        "Масютка О.Ю." : "https://docs.google.com/forms/d/e/1FAIpQLSf28j661LhdyVGW3Il2lFYkFSwS4XU_Y91bl-otpC7Y_Pe5Sg/viewform"
                                    },
                                "ПВС" : \
                                
                                    {
                                        "Коломієць І.С." : "https://docs.google.com/forms/d/e/1FAIpQLSfNhR22TkLqBY4Tfva-7i9kK8ZWzgrgzIRBCXGXRVH-yXyuSQ/viewform"
                                    },
                                "ПРО" : \
                                
                                    {
                                        "Борецький О.Ф." : "https://docs.google.com/forms/d/e/1FAIpQLSfCzDeydGgQS-vAzNNMDxl3gN5MkwTT5Aq0zlKuQYww25kVtQ/viewform"
                                    },
                                "КЛ" : \
                                
                                    {
                                        "Баужа О.С." : "https://docs.google.com/forms/d/e/1FAIpQLSedL6GFuAS8pU3QwGMvVtrQclbU9LmLAnHm26SD7afAY5gcLw/viewform"
                                    },
                                "ЦОС" : \
                                
                                    {
                                        "Барабанов А.В." : "https://docs.google.com/forms/d/e/1FAIpQLSfjDSdaWwHilN7HBYxCXNDu7MTrRqCKsLsc4NrrGPKcqyQkHw/viewform"
                                    },
                                "ТПКС" : \
                                
                                    {
                                        "Барабанов А.В." : "https://docs.google.com/forms/d/e/1FAIpQLSfJ8a0cN_qdHiKGoTRt7i041M4KrVGGQ4g3S4nTjHtgm0_vaA/viewform"
                                    },
                                "Англ" : \
                                
                                    {
                                        "Александрук І.В." : "https://docs.google.com/forms/d/e/1FAIpQLSdtbbc1Ev8kvDhv9XgmPwQvQ5Y0tCezBfZRlCEoDLStfrZ8fQ/viewform"
                                    },
			}
		}
	},
	"пф" : \
	{
		"1" : \
		{
		    	"еітм" : \
			{
				"Англ" : \
                                
                                    {
                                        "Александрук І.В."  : "https://docs.google.com/forms/d/e/1FAIpQLSdB-0P06kk8vdaiiDFuzPeyfU7kNQ7D875tov8lH5U04_wqKw/viewform",
                                        "Борисенко П. А."   : "https://docs.google.com/forms/d/e/1FAIpQLSc-WkFmTHCO5qP97_md66QSa8m-a4pD0AXwiwC3LbUMVYv6xQ/viewform",
                                        "Гонта І.А."        : "https://docs.google.com/forms/d/e/1FAIpQLSchqxILtZVKMikDBbCJTPPfDtgbgdq3bVCoRh00jXUTG0zrbA/viewform",
                                        "Кирилюк О.Л."      : "https://docs.google.com/forms/d/e/1FAIpQLSd_YB2DqNnWFJ4RvNq5AToEPM1jd8-rlmoihja4jnCg7AMfHg/viewform",
                                        "Тарасова В.В."     : "https://docs.google.com/forms/d/e/1FAIpQLSclQc6r-3tIdOn5tUmxMVShrXVXfR4hSGW9e7Z8vKs3oeE0pQ/viewform",
                                        "Титова О.І."       : "https://docs.google.com/forms/d/e/1FAIpQLScUxcsHoUrjYXU0qxzaCkhv41X3p98lc8ENR5ysg9IEy4cr4Q/viewform"
                                    },
                                "ОП" : \
                                
                                    {
                                        "Єфіменко С.В." : "https://docs.google.com/forms/d/e/1FAIpQLSdkGob-8pdUl63QZkvcGQI-dUaEUsAXNoep9AVYX1yFldIkkg/viewform"
                                    },
                                "АПЗ" : \
                                
                                    {
                                        "Колєнов С.О."    : "https://docs.google.com/forms/d/e/1FAIpQLSdCjYywx9KMql4A1m4FFQeWhazrDvLSsSVgI9rNPtnkbTGwmw/viewform"
                                    },
                                "Механіка" : \
                                
                                    {
                                        "Короновський В.Є."     : "https://docs.google.com/forms/d/e/1FAIpQLSdtWCozmt5YKs-HdTXi9XXaGTRZN3XaIxb55q7ZqrggJn5smQ/viewform",
                                        "Слінченко Ю.А."        : "https://docs.google.com/forms/d/e/1FAIpQLSdkiFRfZaGID9T91nE3tTQOKA9UkiS6XZiHEeF1_fmJqkw0jw/viewform",
                                        "Сохацький В.П."        : "https://docs.google.com/forms/d/e/1FAIpQLSd39EVnM0ZmuIaV_P03rpXM2uvKmABpUCjnEFlG7DuNTSbU2A/viewform"
                                    },
                                "ВДУС" : \
                                
                                    {
                                        "Набока С.В." : "https://docs.google.com/forms/d/e/1FAIpQLSdRTsb9Msth3z0v43hlB6hPqWkfX3b_IO8pYVC6Zte0eVsQPw/viewform"
                                    },
                                "МатАнал" : \
                                
                                    {
                                        "Масютка О.Ю." : "https://docs.google.com/forms/d/e/1FAIpQLSd0YosYeYmut6B-hxyBGf-Qu0ewXGq9HNoSHTVkBtqahmRXGg/viewform",
                                        "Моторна О.В." : "https://docs.google.com/forms/d/e/1FAIpQLSeVwpl3WiS9xn-L5DvNFIqRstILFYYiJByYMQ3woSgjKNHn4w/viewform",
                                        "Сугакова О.В." : "https://docs.google.com/forms/d/e/1FAIpQLSdKhpNH1HrKkGTwu661WMw8a61N0k9FNykfcxqbcfQS0qfXvQ/viewform"
                                    },
                                 "Лаб ЕФ" : \
                                
                                    {
                                        "Слінченко Ю.А." : "https://docs.google.com/forms/d/e/1FAIpQLSdps6hj4PIWA8pozI2Q9dumLZtcgvWacN-b1UtA3S1OXLcCcw/viewform",
                                        "Моторна О.В." : "https://docs.google.com/forms/d/e/1FAIpQLSeVwpl3WiS9xn-L5DvNFIqRstILFYYiJByYMQ3woSgjKNHn4w/viewform"
                                    }
                                
                                
			},
                        "еф" : \
			{
				"Англ" : \
                                
                                    {
                                        "Александрук І.В."  : "https://docs.google.com/forms/d/e/1FAIpQLScHkRDgEK5oc3nCKbmVPE9wfMcxCGzoKwDzNk0pDTjI2234XQ/viewform",
                                        "Гонта І.А."        : "https://docs.google.com/forms/d/e/1FAIpQLScFL2Kiz42yb-7byCNNPSamxSEkX2jkV_cEWQcWpcM1C28kkA/viewform",
                                        "Кирилюк О.Л."      : "https://docs.google.com/forms/d/e/1FAIpQLSc-50D2Nquc8nGOiYQHtB_T9PZUkaJGn2xKXdSMeC_M0D0jEw/viewform",
                                        "Тарасова В.В."     : "https://docs.google.com/forms/d/e/1FAIpQLSeKpwKCzIoICHxUcfrq2u4-qlQUTuBjxmKrD1p5XKNdsh_zTA/viewform",
                                        "Титова О.І."       : "https://docs.google.com/forms/d/e/1FAIpQLSca1l6qDU5kNs0oUwZfkmvfadQrsV2kqiM715A2MIRofXFPgQ/viewform"
                                    },
                                "Прога " : \
                                
                                    {
                                        "Єфіменко С.В." : "https://docs.google.com/forms/d/e/1FAIpQLSd1wD0DPBHop5yhEH2RpacR2_m8NNU4iCvOGAMw-eBXpPqxjA/viewform",
                                        "Іваненко Д.О." : "https://docs.google.com/forms/d/e/1FAIpQLSeQmwgKhBvdOrtf7vjWnBITvJHfErvonwhdL-Rs39Nbwworiw/viewform"
                                    },
                                "АПЗ" : \
                                
                                    {
                                        "Колєнов С.О."    : "https://docs.google.com/forms/d/e/1FAIpQLSeddvS_CrCd64ZxsQYA_oGxfU5zpXMlhbuaknxHMHlSnXr0ZA/viewform",
                                        "Попов М.О." : "https://docs.google.com/forms/d/e/1FAIpQLSev4GKqApyPsnQ2IClc7teLg3iARkNI3RP1h79y8Jd_2W__Cg/viewform"
                                    },
                                "Механіка" : \
                                
                                    {
                                        "Коваленко В.Ф."        : "https://docs.google.com/forms/d/e/1FAIpQLSejq_JtjFFONQRoo--FUTfVfr-tgFGiGatOZs6vuBXvmEkU0Q/viewform",
                                        "Сохацький В.П."        : "https://docs.google.com/forms/d/e/1FAIpQLSfgybEM3s7Z8E_ZtEqTkKvpTv-YPHRyx82Fq0jEhZLT_F1dLw/viewform"
                                    },
                                "ВДУС" : \
                                
                                    {
                                        "Набока С.В." : "https://docs.google.com/forms/d/e/1FAIpQLSdBXPtSgpP4k5YA6ZC7BfoPwIbLYDW1EryQ71g6-YmMdz60xw/viewform"
                                    },
                                "МатАнал" : \
                                
                                    {
                                        "Масютка О.Ю." : "https://docs.google.com/forms/d/e/1FAIpQLSd0YosYeYmut6B-hxyBGf-Qu0ewXGq9HNoSHTVkBtqahmRXGg/viewform",
                                        "Моторна О.В." : "https://docs.google.com/forms/d/e/1FAIpQLSeb8ItbZUUrIssPPridUInMJvJ33jozibwH2E_8XEQn9DIVpA/viewform",
                                        "Прощенко Т.М." : "https://docs.google.com/forms/d/e/1FAIpQLScMapW_dWKR__nAm-P4qoDil3gCJsSJujO1H6bT4TXdNOxr8Q/viewform"
                                    },
                                 "Економікс" : \
                                
                                    {
                                        "Савчук Н.В." : "https://docs.google.com/forms/d/e/1FAIpQLSftFOklhPTsQqvy3uWYWW90wB1GO0GRg6zWOwi87xskwUTpxw/viewform"
                                    }
                                
                                
			},
                        "пфнкт" : \
			{
				"Англ" : \
                                
                                    {
                                        "Александрук І.В."  : "https://docs.google.com/forms/d/e/1FAIpQLSfRXfP06LczqYvihaqlY1_K4s-WMdJWd3vMmjEwKm5z2r9KfQ/viewform",
                                        "Борисенко П. А."   : "https://docs.google.com/forms/d/e/1FAIpQLScMh2JH5miEAwexuW_LWvDmKawOjvozdCp3fkwMvCxAolmAGw/viewform",
                                        "Гонта І.А."        : "https://docs.google.com/forms/d/e/1FAIpQLSd0tPRlR81gXRYIsZYr3lrTDHLMfPkWn3ssGdx--wuYYe7_1g/viewform",
                                        "Кирилюк О.Л."      : "https://docs.google.com/forms/d/e/1FAIpQLSfVVawavgY7m6mzKoRWdGziy0OzgOV4IBu-Bbt3btsdmqr5qg/viewform",
                                        "Тарасова В.В."     : "https://docs.google.com/forms/d/e/1FAIpQLSfci_fYukx7ZnWYdUUowcxvFk35Y2yesfEhckx_38p2om9BaQ/viewform",
                                        "Титова О.І."       : "https://docs.google.com/forms/d/e/1FAIpQLSer7tmaBOvmf8Exf-AZG54e6NF-QZ5iY3rkL_GW5isGn7vymg/viewform"
                                    },
                                "Лаб ЕФ" : \
                                
                                    {
                                        "Висоцький М.В." : "https://docs.google.com/forms/d/e/1FAIpQLScewKAbQCObhr2dNQWx2oPZa0I-MYE4FHMpa6Yd2aKIDQr_yA/viewform"
                                    },
                                "ОП" : \
                                
                                    {
                                        "Єфіменко С.В." : "https://docs.google.com/forms/d/e/1FAIpQLSfFKcQzSPBq6w5FV7KZwo8C7WuGMp7L-RJuaWtBWlmJ_p4QTA/viewform",
                                        "Іваненко Д.О." : "https://docs.google.com/forms/d/e/1FAIpQLSeXi6mD3Z72dDHBtqGGDGpFFk817OhTtzN5GmgF0FMqzmtCAg/viewform"
                                    },
                                "Механіка" : \
                                
                                    {
                                        "Коваленко В.Ф." : "https://docs.google.com/forms/d/e/1FAIpQLSd4ohAFHp4nwDDtW43cyeBvkcAEVVOzIJ7JnLc37lYDkWpHoA/viewform",
                                        "Короновський В.Є." : "https://docs.google.com/forms/d/e/1FAIpQLSdICeSk4W8I1e9k1IXftopwPTRiY9JqlWKr83nng9DsOfcxRg/viewform",
                                        "Сохацький В.П." : "https://docs.google.com/forms/d/e/1FAIpQLSeHX0Uq-SBN3pvbNt75XzYptveTr9_ePf_T03AW1a1SBUrM0A/viewform"
                                    },
                                "АПЗ " : \
                                
                                    {
                                        "Колєнов С.О." : "https://docs.google.com/forms/d/e/1FAIpQLSetm4tg5zoG0xSXGHllfr-9BDRZX9FoFGgHLr_1SmisbspVTQ/viewform",
                                        "Попов М.О." : "https://docs.google.com/forms/d/e/1FAIpQLSe5hzmumbWkrVRzdvfQlDth6lT6a3LD5Qpsw3RCzH3a9EiVTg/viewform"
                                    },
                                "МатАнал " : \
                                
                                    {
                                        "Масютка О.Ю." : "https://docs.google.com/forms/d/e/1FAIpQLSdOVXnEpt3M25uABpy7D7URcXNFtVD9l28fVS8lcOMSzXaEQA/viewform",
                                        "Моторна О.В." : "https://docs.google.com/forms/d/e/1FAIpQLSel7K5MsiDpcapPDn9KJbMdsmjSnPhmrIA-S8VnbdxAaBNbAw/viewform",
                                        "Сугакова О.В." : "https://docs.google.com/forms/d/e/1FAIpQLSe6xhm5Fa4fJo5C-bjunojtz222bp_xpMBkkHjtEJJI3pmZkw/viewform"
                                    },
                                "ВДУС" : \
                                
                                    {
                                        "Набока С.В." : "https://docs.google.com/forms/d/e/1FAIpQLSfwg1v8H-XMhb26zC1-07vCqiN8oRN0BSeb77vA92FrgPY-Tg/viewform"
                                        
                                    }
			}
		},
		"2" : \
		{
		    	"none" : \
			{
				"ЕлМаг " : \
                                
                                    {
                                        "Гойса С.М."    : "https://docs.google.com/forms/d/e/1FAIpQLScA-X-eTtQv8i_ygoInx66OqdQv4rrO3orALgZU02vlEfiARg/viewform",
                                        "Іванюта О.М."  : "https://docs.google.com/forms/d/e/1FAIpQLScBsWqYZxLpZirM0oj2XlXWqlDYZNvwNJNjqYUev0DxZVUmrA/viewform",
                                        "Іщук Л.В."     : "https://docs.google.com/forms/d/e/1FAIpQLSdSbK34sziLlqWCc3aIBBwBmtbvBU4o57m5N0XlSTnlQrhMpw/viewform",
                                        "Слінченко Ю.А.": "https://docs.google.com/forms/d/e/1FAIpQLSfe1f0v6l1UrfqYDVuGdHeWLHUFPredImSl0CvAUXs4gPoHfQ/viewform"
                                    },
                                "Лаб ЕФ" : \
                                
                                    {
                                        "Гойса С.М." : "https://docs.google.com/forms/d/e/1FAIpQLSestAqr9CgKXVaU6YrGYXh-QMeAOHCJVWz07MpInXvJez8uGg/viewform",
                                        "Слінченко Ю.А." : "https://docs.google.com/forms/d/e/1FAIpQLSc892xeLqJ6nRzc88JK5GAwWGvkIDcNcSfZDz7wZ3DiH9hYEw/viewform"
                                    },
                                "Філософія" : \
                                
                                    {
                                        "Загороднюк В.В." : "https://docs.google.com/forms/d/e/1FAIpQLScAV-XzTtoF_OcCC332ZULzGxDyJkEO5hnfjnSuBEZhrbFeCQ/viewform",
                                        "Павлов Ю.В." : "https://docs.google.com/forms/d/e/1FAIpQLSeaPXsCDGT2fPCvhH_oMgrxdVs30lNsL1oRJKJFwlp-XKBiig/viewform"
                                    },
                                "ТеорМех " : \
                                
                                    {
                                        "Іванов Б.О." : "https://docs.google.com/forms/d/e/1FAIpQLSffzgJCBzoRf57K4ZxWDJLswqHVr5IskzqqVnlIid0ayxKDag/viewform",
                                        "Максюта М.В." : "https://docs.google.com/forms/d/e/1FAIpQLSfLsDHUzcYQVS91L5ehDSXGJYFU4rdP619daUDuPEgHE-ze8Q/viewform",
                                        "Ястремський І.О." : "https://docs.google.com/forms/d/e/1FAIpQLScEB5yxfFmmMAMo6FjNllRzZ4oIw7tzd3wHGAaPdYRvkftMtQ/viewform"
                                    },
                                "МОДЧМ " : \
                                
                                    {
                                        "Комаров І.В." : "https://docs.google.com/forms/d/e/1FAIpQLSdIjfwxP8xXfxEn_DZZCFykd8KOiZNLJJgpIq35CaQVqOLSIA/viewform",
                                        "Оберемок Є.А." : "https://docs.google.com/forms/d/e/1FAIpQLSe_Zhyi1MwpUl9GLoFqyxXTYutmBvZBpyTSzmNppmTbhE7prw/viewform",
                                        "Прощенко Т.М." : "https://docs.google.com/forms/d/e/1FAIpQLSc0_O8z1TTsgR8ZQe-18oo1rSEaK-PJR8nqITxaFjKBDOy5Nw/viewform"
                                    },
                                "РТКС " : \
                                
                                    {
                                        "Куцик А.М." : "https://docs.google.com/forms/d/e/1FAIpQLSfjr6_YMalzXuLSYjxev7dK47q8SEpidCbL27eZE3lhQEok7A/viewform",
                                        "Слюсаренко І.І." : "https://docs.google.com/forms/d/e/1FAIpQLSdaxmYDzEp54BX6RyfFuHYYqgvg2RGF6IGTnVDrFD9ANG1-Pw/viewform",
                                        "Фесенко С.О." : "https://docs.google.com/forms/d/e/1FAIpQLScQTxKUuGAe59X3brkZ-DgVtVV92IAUNI66yUEH-qaObUSDzw/viewform"
                                    },
                                "ММФ" : \
                                
                                    {
                                        "Максюта М.В." : "https://docs.google.com/forms/d/e/1FAIpQLSf5BlShuhzrYkv_YD0gzWDghzrDPrqW6tJbsiIHAJCszG9ZWA/viewform",
                                        "Шека Д.Д." : "https://docs.google.com/forms/d/e/1FAIpQLSdqdW8PuEcE3cdl30QhiAadHED4qTEG-gOWm2AGG4io91MQTQ/viewform",
                                        "Ястремський І.О." : "https://docs.google.com/forms/d/e/1FAIpQLScQrQ7WpmIyDPnAspIBT8Z4mM3LqjDW6NC85-3GBsdoZmDvDg/viewform"
                                    },
                                "ДифТЙ " : \
                                
                                    {
                                        "Масютка О.Ю." : "https://docs.google.com/forms/d/e/1FAIpQLScXb6n_HuNgBLCsGS3-TRtGGx-i-6YQDwyaFgcxPklidBZetg/viewform",
                                        "Моторна О.В." : "https://docs.google.com/forms/d/e/1FAIpQLSdS5DwMmgNQtHZ2EO3r8uXt9ehgjU-FgZTvgcc6yU7p0I5-jQ/viewform",
                                        "Сугакова О.В." : "https://docs.google.com/forms/d/e/1FAIpQLScVqEUibsSq3oUP1XWclvNWRaxe3afcklVQmJ1wOJmcZuQVQA/viewform"
                                    },
			}
		},
		"3" : \
		{
		    	"none" : \
			{
				"Коливання " : \
                                
                                    {
                                        "Анісімов І.О."  : "https://docs.google.com/forms/d/e/1FAIpQLSeI5rb5HL2i67YtROgNojz_dKaW7fFaSZUuZZBWKKEtv082NQ/viewform",
                                        "Горячко А.М."   : "https://docs.google.com/forms/d/e/1FAIpQLSc3uQ7tvJD-ZvCK5eC3tfDc4VhVe838B6jeOLHy6GYi0so0Uw/viewform"
                                    },
                                "Культура " : \
                                
                                    {
                                        "Вдовиченко Г.В." : "https://docs.google.com/forms/d/e/1FAIpQLSe2-qMoLeZEnh70vv0e0Z5glt5Kv5i-GlMATN49PWdltUn6UQ/viewform"
                                    },
                                "Квант " : \
                                
                                    {
                                        "Висоцький В.І." : "https://docs.google.com/forms/d/e/1FAIpQLSeL17O_ULV-LxrtfstNBan8AU9rDhJU40kTmIRU6kMEuBb3qg/viewform",
                                        "Максюта М.В." : "https://docs.google.com/forms/d/e/1FAIpQLSeFjtaGAITyAc8XkTnEmaq30VMve_DqVS6GIIaVv1KXmZ6Dag/viewform"
                                    },
                                "Атомка " : \
                                
                                    {
                                        "Карлаш Г.Ю." : "https://docs.google.com/forms/d/e/1FAIpQLSd_U2en61xHHDghAID_0nNVtivrBtHFc3ZUsl_cPESPqiUiUg/viewform",
                                        "Ніконова В.В." : "https://docs.google.com/forms/d/e/1FAIpQLSfNvULYEk7lJit0_I3cjSMHNauT0sxAcexXKBYDTBfynJgM1A/viewform",
                                        "Овечко В.С." : "https://docs.google.com/forms/d/e/1FAIpQLSfx50_vX3BTiDQeSl_qHxs6acEnoaCva0Kp0nw9Zg8iFsg1yA/viewform"
                                    },
                                "ЛабЕкспФіз" : \
                                
                                    {
                                        "Коломієць І.С." : "https://docs.google.com/forms/d/e/1FAIpQLSf8-CT_dhDi9_bhufAKJvtxHBOw5N08P2epnuvn7X3-tZXjOQ/viewform",
                                        "Короновський В.Є." : "https://docs.google.com/forms/d/e/1FAIpQLSd2BaftO_vYwRUjQSmbJLfOQB3G9wsniW4h2x0sz2RX31kBZg/viewform"
                                    },
                                "Культура " : \
                                
                                    {
                                        "Мураткіна Т.М." : "https://docs.google.com/forms/d/e/1FAIpQLSeDfJose61qGQ_-3rdljheGcU0t7r796tOgtUjajza1ygqR8Q/viewform"
                                    },
                                "Електродинаміка " : \
                                
                                    {
                                        "Нетреба А.В." : "https://docs.google.com/forms/d/e/1FAIpQLScCpIbhfsx99hdQ_vnDDFMhGJ-ovGlvYo9CPHenSUQj42r1SA/viewform",
                                        "Обуховський В.В." : "https://docs.google.com/forms/d/e/1FAIpQLSdd9GLDArP8_TUZYru22xnZhCcNGZ1c58I_O-8c0KkJ5O6lOQ/viewform",
                                        "Ястремський І.О." : "https://docs.google.com/forms/d/e/1FAIpQLSf69Wn8-18CkcFUpOm1u5S4NEfmQ2DSyL_-ARcSaW8CO6u-vg/viewform"
                                    },
                                "СоцПолСт " : \
                                
                                    {
                                        "Петренко В.В." : "https://docs.google.com/forms/d/e/1FAIpQLSd8ABXP5RsVsj_85VTRbKG_FVbr31Ue7pTtg--Y8n6SgCm5lQ/viewform"
                                    },
			}
		},
		"4" : \
		{
		    	"крф" : \
			{
				"КРФЕ " : \
                                
                                    {
                                        "Гайдай Ю.О." : "https://docs.google.com/forms/d/e/1FAIpQLSeMCOplw65EMHYWLvxDy7F6CnebNkKvafByvCM3sb8ZwHWTVw/viewform"
                                    },
                                "Англ " : \
                                
                                    {
                                        "Гонта І.А." : "https://docs.google.com/forms/d/e/1FAIpQLSdmiQk-uWPI34In4C6--a3P2fysAJi3uxUz1QG0tHxC0-wchg/viewform"
                                    },
                                "Мікро ЕлДин" : \
                                
                                    {
                                        "Зависляк І.В." : "https://docs.google.com/forms/d/e/1FAIpQLSc5Fq-WNy_CL5db5n1T5NnayDru7vUJUsGmf3Gay63UJTPM-w/viewform"
                                    },
                                "Лаб КР" : \
                                
                                    {
                                        "Загородній В.В." : "https://docs.google.com/forms/d/e/1FAIpQLScPjdBq51P-XvoWinO51e8CxrN7icqPby7Bap2Tq6jiOxU7LA/viewform"
                                    },
                                "ФЛЕл " : \
                                
                                    {
                                        "Кисленко В.І." : "https://docs.google.com/forms/d/e/1FAIpQLScKheJOoRmEUkGFEa3NK9Vn0pVCQAe6MIE7snJNDzR08spUYg/viewform",
                                        "Нечипорук О.Ю." : "https://docs.google.com/forms/d/e/1FAIpQLSdlyFcsGChNlglqAjSSU8mhIw0A5BiAIErH-zZo1cyMC-Hn8w/viewform"
                                    },
                                "Статфіз" : \
                                
                                    {
                                        "Коваленко А.В." : "https://docs.google.com/forms/d/e/1FAIpQLSeHWtB3i-PnzbSnmT5COkD3QC8OVFpOCz551NnEB23SepbjAg/viewform"
                                    },
                                "Лаб КРФ" : \
                                
                                    {
                                        "Нечипорук О.Ю." : "https://docs.google.com/forms/d/e/1FAIpQLSfmVL3MsVFjA2eS-UAV1ArM52D1zjaE5U0r56z93BO6GSjqqQ/viewform"
                                    },
                                "Мікропроцесори " : \
                                
                                    {
                                        "Смирнов Є.М." : "https://docs.google.com/forms/d/e/1FAIpQLSds3rTpUATrdbYRdaUq5GdWk-dfqySzA9M3LOB94HEVFePx-Q/viewform"
                                    },
			},
                        "мрф" : \
			{
				"КомпЕксп " : \
                                    {
                                        "Веремій Ю.П." : "https://docs.google.com/forms/d/e/1FAIpQLSe8f_npkRBGjMfxI1PnmW3MF1X6VErNXzgBoRPFbEQw0xzQng/viewform"
                                    },
                                "Лаба МРФ" : \
                                
                                    {
                                        "Веремій Ю.П." : "https://docs.google.com/forms/d/e/1FAIpQLSftcYqtp8KVc0vf6dWUJ_dC81j0czFJuU1u3kc7gmy4nQT5fw/viewform",
                                        "Іванісік А.І." : "https://docs.google.com/forms/d/e/1FAIpQLSf1Otx6LsAQFNGReI3VgO9zULHdlMuoC0Vm2IiblUivqX_RTA/viewform"
                                    },
                                "Фізи " : \
                                
                                    {
                                        "Веремій Ю.П." : "https://docs.google.com/forms/d/e/1FAIpQLSdBEiWCM6w-cfRxn75ceUSMgqLms3isFAFN1vlREeoYQOMKdg/viewform",
                                        "Радченко С.П." : "https://docs.google.com/forms/d/e/1FAIpQLSd0STfPPZr1cTBaeUjBihxWGgLXwyYdjOn8FbSJcLzJxD62Dw/viewform"
                                    },
                                "МР " : \
                                
                                    {
                                        "Радченко С.П." : "https://docs.google.com/forms/d/e/1FAIpQLScshLYMmOy9LbATiIyFM1ZWyr-_BqZ0ZJpYgoOX1BU7kAAngw/viewform"
                                    },
                                "Біофіз" : \
                                
                                    {
                                        "Лук'янець О.О." : "https://docs.google.com/forms/d/e/1FAIpQLSeuIA-rimknFA4171PUIYN0yBTYUSd4Ip1xAUGj2bLG-wXTaw/viewform"
                                    },
                                "КвНпЕл " : \
                                
                                    {
                                        "Іванісік А.І." : "https://docs.google.com/forms/d/e/1FAIpQLSfbxUEWrZVO5x8pTmsSEOkmSF_17p-vEaZkjC9xafJWCAmp2w/viewform",
                                        "Євтух А.А." : "https://docs.google.com/forms/d/e/1FAIpQLSdqiVVOqZOXxVOGeclmE2WB5hbKnMkbLlAUmYPSa9f2FsJ06A/viewform"
                                    },
                                "Анатомія " : \
                                
                                    {
                                        "Давидовська Т.П." : "https://docs.google.com/forms/d/e/1FAIpQLScXWr0brUuu1XBdy2qKdeOTwZy9WLgTimUjffIONjQLAnPZqw/viewform"
                                    },
                                "Англ " : \
                                
                                    {
                                        "Гонта І.А." : "https://docs.google.com/forms/d/e/1FAIpQLSfLjK4H_pKL0KxsvER-387tw04gOvdQW_qoWVAGjKpXXkVOlA/viewform"
                                    },
			},
                        "нфне" : \
			{
				"Англ" : \
                                
                                    {
                                        "Александрук І.В." : "https://docs.google.com/forms/d/e/1FAIpQLSfnPGfozT8ZJrcDbgRURD_a_b9sYbR9iTfye65Bpuc6lwWlkA/viewform"
                                    },
                                "ТОФН " : \
                                
                                    {
                                        "Будник М.М." : "https://docs.google.com/forms/d/e/1FAIpQLSf-VYS7nOHuR-GcU4te3XsI9tTPaiZzHJXKtI4rgq0XyipszQ/viewform",
                                        "Кулик С.П." : "https://docs.google.com/forms/d/e/1FAIpQLScb7KMa-HLjOPcag28aC-dsiKXhcygYcmlYZn3MOIMLS6s8uA/viewform"
                                    },
                                "ЦСЗ " : \
                                
                                    {
                                        "Коваленко А.В." : "https://docs.google.com/forms/d/e/1FAIpQLSfMmV7fTtYtGzGwUTvS1uk6nqgA5PlFpt5c3RQEpVh_3c_7DA/viewform"
                                    },
                                "Твердофіз " : \
                                
                                    {
                                        "Кулик С.П." : "https://docs.google.com/forms/d/e/1FAIpQLScF6oQdRPGSznRdS1zMaltgt_Y8UOJY4XrCDvzYKDUd7ypfIg/viewform",
                                        "Курашов В.Н." : "https://docs.google.com/forms/d/e/1FAIpQLScluSNdEDyciRWADRDtYK7-NuAR0TGSZnWbOhu0O0XShJ-UnQ/viewform"
                                    },
                                "Лаб Нано" : \
                                
                                    {
                                        "Малишев В.Ю." : "https://docs.google.com/forms/d/e/1FAIpQLScbwPEfuxAi1zXnosqP48sycSRsXiMirEnHMjEhlSehEoH69A/viewform"
                                    },
                                "Мікро ЕлДин" : \
                                
                                    {
                                        "Прокопенко О.В." : "https://docs.google.com/forms/d/e/1FAIpQLSdw0D18nVRZPxMIgrcxxtBvXxhFqzkm5qQRgV2qHavpmIFpKw/viewform"
                                    },
                                "Кріог " : \
                                
                                    {
                                        "Пустовіт Ю.В." : "https://docs.google.com/forms/d/e/1FAIpQLSeSG9xzhggqOEnna-odTbrQrV2YR7sgZrzsw2frvLvJt_9WQQ/viewform"
                                    },
			},
                        "фе" : \
			{
				"Англ " : \
                                
                                    {
                                        "Александрук І.В." : "https://docs.google.com/forms/d/e/1FAIpQLSfnAoof2YV4RSEtQgslAJkFEFyCtz9Y7hyuY-IZ8i29gRYJyA/viewform"
                                    },
                                "Плазма " : \
                                
                                    {
                                        "Анісімов І.О." : "https://docs.google.com/forms/d/e/1FAIpQLSdKpWKWMLGZFZRrK49jurph5Lsc3e9Skyzw5V51euZNgdaHXw/viewform"
                                    },
                                "АЗП " : \
                                
                                    {
                                        "Веклич А.М." : "https://docs.google.com/forms/d/e/1FAIpQLSfjbMBBgxN-TyKsu_2UT4szfKGyUOMExmzDf96yK51_PF2JFQ/viewform"
                                    },
                                "СКНЕ " : \
                                
                                    {
                                        "Вербицький В.Г." : "https://docs.google.com/forms/d/e/1FAIpQLScTGpUttTJ7Tw9S8zEhnEPciywDTQAzp3YhkobjUEYaHUquJQ/viewform",
                                        "Іванісік А.І." : "https://docs.google.com/forms/d/e/1FAIpQLSeIJ8qJ5_sJnHgXYpwHHEMTDt-kpo2GlGArMo37qOO6aZoybA/viewform"
                                    },
                                "Статфіз " : \
                                
                                    {
                                        "Кравченко О.Ю." : "https://docs.google.com/forms/d/e/1FAIpQLSfVjb72qAZJQ0wyGX3jtgXv6NI2g0BFzOp8vA09DdRlZeHO0w/viewform"
                                    },
                                "Лаб ФЕ" : \
                                
                                    {
                                        "Недибалюк О.А." : "https://docs.google.com/forms/d/e/1FAIpQLSdOv6V5-qi0j18BzM3O0YCwM_19nDZHPHxxH1H0Z9QI-FmSOw/viewform"
                                    },
                                "Мікрохв " : \
                                
                                    {
                                        "Недибалюк О.А." : "https://docs.google.com/forms/d/e/1FAIpQLSdvBtnuMFPhMRAW5FtSOJVQeMgH7GzpiA1In7o0sajaCFF_bA/viewform",
                                        "Ольшевський С.В." : "https://docs.google.com/forms/d/e/1FAIpQLScYaXQBUsUuo500GRK19syo4QBltWebN8KFYukVku1scjVagA/viewform"
                                    },
			}
		}
	},
	"рт" : \
	{
		"1" : \
		{
		    	"ібтксм" : \
                        {
				"ЗагФіз " : \
                                
                                    {
                                        "Іщук Л.В." : "https://docs.google.com/forms/d/e/1FAIpQLSfBxDZ0Gm5mxKAZpvZYeE6LpOpZsS0mgNVn0JeaMDvScYiOnw/viewform",
                                        "Коваленко В.Ф." : "https://docs.google.com/forms/d/e/1FAIpQLScs3c6T68FuFBP9UyVJFj-mBGx9SDWRL99PxsauPNYDWLbjeQ/viewform",
                                        "Коломієць І.С." : "https://docs.google.com/forms/d/e/1FAIpQLSd_wt2hx1fPWfu8lCzE9cOEfLdqyqxtE77zUe-Z_ynM6BprWA/viewform",
                                        "Сохацький В.П." : "https://docs.google.com/forms/d/e/1FAIpQLSe8hhTeJRADLiZMa15-eYRLBnVky6Xr4JY7L4j-nS6hQMvFGw/viewform"
                                    },
                                "Прога " : \
                                
                                    {
                                        "Кононов М.В." : "https://docs.google.com/forms/d/e/1FAIpQLSf8Wf7eKP00t87zvKxyKBh3sigpF5g4GOGcz0UFS2ptixK8Mg/viewform",
                                        "Куцик А.М." : "https://docs.google.com/forms/d/e/1FAIpQLScZgJJX-8gMugKbUAZsnI4skXKeOjbjd8kowSMIV-SQ_lPdYg/viewform"
                                    },
                                "Вишмат " : \
                                
                                    {
                                        "Кривошия С.А." : "https://docs.google.com/forms/d/e/1FAIpQLSfh9Cwh7d5eBpk3JIu1jfJ2QiX4lpbowLzp5BO0mFjK4pNd5Q/viewform"
                                    },
                                "ВДУС" : \
                                
                                    {
                                        "Набока С.В." : "https://docs.google.com/forms/d/e/1FAIpQLSdocdH2Z6w8PF8aRhES86psw1YR8nEDKZc_28jRKfdKxt4smA/viewform"
                                    },
                                "Англ " : \
                                
                                    {
                                        "Янчук С.Я." : "https://docs.google.com/forms/d/e/1FAIpQLSdxcKxHTbPvIsSLc-YEtDAGUw9EITH1qNRdlLiweKEzMWTuZw/viewform"
                                    }
			},
                        "ібтксм(мс)" : \
                        {
				"Англ " : \
                                
                                    {
                                        "Безпаленко А.М." : "https://docs.google.com/forms/d/e/1FAIpQLSdX1BxNYXWJdAxgNAAgdbCnyiQzVKvtxx-3YeQYD0GiiehNAw/viewform",
                                        "Рєзнікова Н.В." : "https://docs.google.com/forms/d/e/1FAIpQLSdYqUo2WKNyVvgkcYBLaYKRMq3x7IIR61bSMXB14iT4N1bq8w/viewform"
                                    },
                                "Вишмат " : \
                                
                                    {
                                        "Єфіменко С.В." : "https://docs.google.com/forms/d/e/1FAIpQLSeLvAfI17pZWFxQbEvJzu4nCXLHFDNEmFqQAOAfI78U321o8w/viewform",
                                        "Жеребко Т.М." : "https://docs.google.com/forms/d/e/1FAIpQLSesH5JQ4mXOizR0B7kPOfJlJgwfaz2aHgEg2RNuLihwC48BVw/viewform",
                                        "Масютка О.Ю." : "https://docs.google.com/forms/d/e/1FAIpQLScF3nGPgXBSZp5UTx8VtTHh9q1pxYRQPXnKDtxEYlFgwbpUww/viewform"
                                    },
                                "Прога " : \
                                
                                    {
                                        "Кононов М.В." : "https://docs.google.com/forms/d/e/1FAIpQLSehyXcVudhcjSgzXCGDgNRAJmhPfSSSR2b5VdoEA5vWGGIU5A/viewform",
                                        "Куцик А.М." : "https://docs.google.com/forms/d/e/1FAIpQLSfAzVk70DlyA0gS8nlJlScOU_AxoE42gL7GgMeLhcmv5zNtWQ/viewform"
                                    },
                                "ВДУС " : \
                                
                                    {
                                        "Набока С.В." : "https://docs.google.com/forms/d/e/1FAIpQLSe5WX-oVmKXc_IdOg4cN7i0wNlxpV949HRCHHs1Jaso6Bt9kg/viewform"
                                    },
                                "ЗагФіз " : \
                                
                                    {
                                        "Ніконова В.В." : "https://docs.google.com/forms/d/e/1FAIpQLSeiYS9Yrd6G3JxXzj2LtgjDcGwiZTd2EHBTHKc2EjhWBoVXdA/viewform",
                                        "Фелінський Г.С." : "https://docs.google.com/forms/d/e/1FAIpQLSfeeZO2WBlNBsOgbTszGvUo886DCX0uXa_rSYPkIPncXg0DuQ/viewform"
                                    },
                                "ЛМП " : \
                                
                                    {
                                        "Овечко В.С." : "https://docs.google.com/forms/d/e/1FAIpQLSd5SRtt5XOSbFUOvjcREdS9I6AfoHJSpHyG2iE7Xsi-mTk9vA/viewform"
                                    }
			},
                        
		},
		"2" : \
		{
		    	"ібтксм" : \
                        {
				"КБРЗ " : \
                                
                                    {
                                        "Борецький В.Ф." : "https://docs.google.com/forms/d/e/1FAIpQLSdqXhuCGsO8k7cMkt5ibJUfj2YXOQ580arD3OvgWrv9P6Vn5A/viewform"
                                    },
                                "Філософія " : \
                                
                                    {
                                        "Загороднюк В.В." : "https://docs.google.com/forms/d/e/1FAIpQLSeY_lBcYZpEp0Yj52V2zhDOhhjqbjkc3o1u0ttaH_sKyX2O5A/viewform",
                                        "Павлов Ю.В." : "https://docs.google.com/forms/d/e/1FAIpQLSdNg8tum7XyU87WObYYINsIOyp3LAIq8Aor_jGunFYaxQxK4w/viewform"
                                    },
                                "ОТК " : \
                                
                                    {
                                        "Куцик А.М." : "https://docs.google.com/forms/d/e/1FAIpQLScMqaJU2qGGvGPtAvxKaWY5pZSSOU3kh9Pw3lE58ch6AZajIg/viewform"
                                    },
                                "Вишмат " : \
                                
                                    {
                                        "Масютка О.Ю." : "https://docs.google.com/forms/d/e/1FAIpQLSfkB-ucIewSZ5R6YJia-v-ZQWUIu1qb_qi1-F53R6EX3MagFA/viewform"
                                    },
                                "МтР " : \
                                
                                    {
                                        "Рєзніов М.І." : "https://docs.google.com/forms/d/e/1FAIpQLSc8IDNIcj35J1BbEAHCuaMg8uTzDhy3Q_ui3XcqYr3uvDkRrA/viewform",
                                        "Фесенко С.О." : "https://docs.google.com/forms/d/e/1FAIpQLSf-KYAy5-tOAjm7-EBy23o5Y0GCgOWPNmPCA6wagnIK3_FJZw/viewform"
                                    }
			},
                        "пазіб(мс)" : \
                        {
				"КБРЗ " : \
                                
                                    {
                                        "Борецький В.Ф." : "https://docs.google.com/forms/d/e/1FAIpQLSe9SUhsbTmWZKgDnnbKvbg0V-bAHf4y1EbxzWqEQc6gIbeVzA/viewform"
                                    },
                                "ОТАУ " : \
                                
                                    {
                                        "Жиров Г.Б." : "https://docs.google.com/forms/d/e/1FAIpQLSd60iHFPKYx05paERwZaQjIUuWAl6tvIeb9WpVCdeV8UuCuOg/viewform"
                                    },
                                "ЕПР " : \
                                
                                    {
                                        "Нетреба А.В." : "https://docs.google.com/forms/d/e/1FAIpQLScAwyIPB7arVIgqwuVJwITunbXyjpATwVIIRxCFs10_MXmXgQ/viewform"
                                    },
                                "СПР " : \
                                
                                    {
                                        "Четверіков І.О." : "https://docs.google.com/forms/d/e/1FAIpQLSfPcGknM42q4c6LrLrod9TB6O-LtrZsthkMj3rRs5L2nKFnqw/viewform"
                                    },
                                "Вишмат " : \
                                
                                    {
                                        "Ястремський І.О." : "https://docs.google.com/forms/d/e/1FAIpQLSdjUE9O49OwqCOBoGwKO21zyqc1Xr6GO0lSli0mF9V12YG1OA/viewform"
                                    },
			},
                        "пазтк(мс)" : \
                        {
				"КБРЗ " : \
                                
                                    {
                                        "Борецький В.Ф." : "https://docs.google.com/forms/d/e/1FAIpQLSfU_MwGnMBSkfyyQbYsGFrhZDXVT_OmgT3D8G1cNaiVgRLWUw/viewform"
                                    },
                                "ОТАУ " : \
                                
                                    {
                                        "Жиров Г.Б." : "https://docs.google.com/forms/d/e/1FAIpQLSfOO9bOpWnhN4duFr_JWF1K-GptIIg1kLMcrInCfHMBSiNJBA/viewform"
                                    },
                                "ППТС " : \
                                
                                    {
                                        "Кононов М.В." : "https://docs.google.com/forms/d/e/1FAIpQLSeTE6gcOzupidYaoN-9V2SoUBzmknKrK828W6-wlpAxFq657w/viewform"
                                    },
                                "ЕПР " : \
                                
                                    {
                                        "Нетреба А.В." : "https://docs.google.com/forms/d/e/1FAIpQLSc71zMajvoofU99nkvafcefR8gHaGluLE_KVpWZN58zkm0_8A/viewform"
                                    },
                                "Диск " : \
                                
                                    {
                                        "Ральченко С.А." : "https://docs.google.com/forms/d/e/1FAIpQLScoUZ0OiUyhTOpSUziwoMtJh7IF3NCD67m2wbfclHfcpavkTQ/viewform"
                                    },
                                "Вишмат " : \
                                
                                    {
                                        "Ястремський І.О." : "https://docs.google.com/forms/d/e/1FAIpQLSfCYU1Z-hVPWw50KP8xnKQWAe56vkDI0vBk7sC7l466KC_EAg/viewform"
                                    },
                                
			},
		},
		"3" : \
		{
		    	"пазіб" : \
                        {
				"ОТПІ " : \
                                
                                    {
                                        "Аль Шурайфі М.Т." : "https://docs.google.com/forms/d/e/1FAIpQLScZUvASuKSYORNjSuiH_P0pVv5T6dEJN1GeqISyqd2CBk3-vA/viewform",
                                        "Ольшевський С.В." : "https://docs.google.com/forms/d/e/1FAIpQLSeS2QvgDvqGfr6hqAl_qTjhkPwms4qJPfWgavEz-iXw3bKPWQ/viewform"
                                    },
                                "АУП " : \
                                
                                    {
                                        "Бех І.І." : "https://docs.google.com/forms/d/e/1FAIpQLSf5Yl2uCVYvUhenh_beMuxg8u1ZZGBeu43H7kKByWMOVDrzrQ/viewform"
                                    },
                                "ЦСтЕ " : \
                                
                                    {
                                        "Борецький В.Ф." : "https://docs.google.com/forms/d/e/1FAIpQLSdBQL6Hstc0DpoYUcqvvLA4t2QyWGebaI-00peOcaaJD0ahmg/viewform"
                                    },
                                "УЗК " : \
                                
                                    {
                                        "Вдовиченко Г.В." : "https://docs.google.com/forms/d/e/1FAIpQLScIQD5YtML98eXwtmPRP8sKcyE1wXGvfhSsWeUlrixiQHYl0A/viewform",
                                        "Мураткіна Т.М." : "https://docs.google.com/forms/d/e/1FAIpQLSfGJGCNh_wBVI6enTSqNjAkhm6uOon5wzkjs60KNnz7Nz-hkg/viewform"
                                    },
                                "СоцПолСт " : \
                                
                                    {
                                        "Внучко С.М." : "https://docs.google.com/forms/d/e/1FAIpQLSf6VV9t8-5a4VDXu2eEL1d9LliX3fJ7CwBzUos1RwyWJBHtWg/viewform"
                                    },
                                "СПР " : \
                                
                                    {
                                        "Куцик А.М." : "https://docs.google.com/forms/d/e/1FAIpQLSf9uqdvvzCfP3mzhgRFBMF7zqBvZOsK_V8klKugTtTpAG1dmg/viewform",
                                        "Четверіков І.О." : "https://docs.google.com/forms/d/e/1FAIpQLScGxbXsfPgKRz9lcd6xf5S9d0kl2tT_skha3-kw2rj3kDJufA/viewform"
                                    }
			},
		},
		"4" : \
		{
		    	"пазіб" : \
                        {
				"ОБЗ " : \
                                
                                    {
                                        "Довбня С.Я." : "https://docs.google.com/forms/d/e/1FAIpQLSdsAc3xtX8UDKTU_B14NSsL9g1c8MqaFPEWbeqB1GrjNqOd5g/viewform"
                                    },
                                "ПОС " : \
                                
                                    {
                                        "Дружинін В.А." : "https://docs.google.com/forms/d/e/1FAIpQLSfkGzdbjW9K3zRBWZeAyOxKx9Eu6poDP3Gi5u3Wq0zy0TFBpg/viewform"
                                    },
                                "ЕКПМД " : \
                                
                                    {
                                        "Малышев В.Ю." : "https://docs.google.com/forms/d/e/1FAIpQLSeShpq-Dg3s1YseEqHBFOGHchUwEqv6XnXSYEY8m_Jh1Vwz_w/viewform",
                                        "Прокопенко О.В." : "https://docs.google.com/forms/d/e/1FAIpQLSfpnV-TnY0M-Vzaloz615-MUd3NYZjxqxmNlNWavh-gqRyDhQ/viewform"
                                    },
                                "СР " : \
                                
                                    {
                                        "Обуховський В.В." : "https://docs.google.com/forms/d/e/1FAIpQLSe_K6HGzoaJ2WyFWVmqzNxGUKBWNeXVf2buDKfDJ3ifp6piXg/viewform"
                                    },
                                "КТРЗ " : \
                                
                                    {
                                        "Смирнов Є.М." : "https://docs.google.com/forms/d/e/1FAIpQLSdQPcdosz2GHMZMXk_VBh97XkA-ECqok6cjRGXKohoR5Roz9A/viewform"
                                    },
                                "Англ " : \
                                
                                    {
                                        "Рєзнікова Н.В." : "https://docs.google.com/forms/d/e/1FAIpQLSc42vlpHorYqbzx0e_CpT7mSG4KXTAS-Q_SVi6JPISmdfmF9g/viewform"
                                    },
                                "АСТМД " : \
                                
                                    {
                                        "Слюсаренко І.І." : "https://docs.google.com/forms/d/e/1FAIpQLSdlAk1NJ-ggAGpnIt7UpnExB069ef-EckqlrOu8qQg4yRAF4g/viewform"
                                    },
			},
                        "пазтк" : \
                        {
				"ЗМДАСТ " : \
                                
                                    {
                                        "Аль Шурайфі М.Т." : "https://docs.google.com/forms/d/e/1FAIpQLScOWmzxoX-a9IYESARK6oXY6xDHKZyLFZ5QkcmKzzsPQHZ-_Q/viewform"
                                    },
                                "ПЛД " : \
                                
                                    {
                                        "Аль Шурайфі М.Т." : "https://docs.google.com/forms/d/e/1FAIpQLScFKLTAou0UjtB0qzoHCG10Jf0OSyq52FaRgBI1zs98pbAJjQ/viewform"
                                    },
                                "Англ " : \
                                
                                    {
                                        "Безпаленко А.М." : "https://docs.google.com/forms/d/e/1FAIpQLSfpVgIgeWezNEN8tnafmxt3Qg1TOYHgGZMbioU-1OglUzMzfw/viewform"
                                    },
                                "ОБЗ " : \
                                
                                    {
                                        "Довбня С.Я." : "https://docs.google.com/forms/d/e/1FAIpQLSdXrRirhYeNs-_lPG0dmGyoADqBRtRXzByBxwnpPgo8nHrCRA/viewform",
                                        "Четверіков І.О." : "https://docs.google.com/forms/d/e/1FAIpQLSfFKNmQ0rXZXz7NPJSoZcoX9ESwJE5Uomp90RZ_g6GYvwXjGQ/viewform"
                                    },
                                "ПОСТС " : \
                                
                                    {
                                        "Кельник О.І. " : "https://docs.google.com/forms/d/e/1FAIpQLScXD6nPL2BK_cJe8yHhmZg0wWi5Ay441DlzWT9mJ4P0UAOb1A/viewform"
                                    },
                                "ПЗТ " : \
                                
                                    {
                                        "Кононов М.В." : "https://docs.google.com/forms/d/e/1FAIpQLSdEJRR7LrJxbWzoQbU3e7QgGBpCXZnyEqbIROvgwbyCtElHPw/viewform"
                                    },
                                "ТКОС " : \
                                
                                    {
                                        "Тримбовецкий М.П." : "https://docs.google.com/forms/d/e/1FAIpQLSeXesyhnxQkJGHzfNQ21htPtOr-cadoonKR20oHsAjPAiPpDA/viewform",
                                        "Фелінський Г.С." : "https://docs.google.com/forms/d/e/1FAIpQLSe2fI9kknkrJbGSconc7V3fpSFdwU1_9xFmPBYrbaf9hBWG5A/viewform"
                                    }
			},
                        "рзтк" : \
                        {
				"ЕСРЗ " : \
                                
                                    {
                                        "Аль Шурайфі М.Т." : "https://docs.google.com/forms/d/e/1FAIpQLSd-EucjvPGCcL0YhXyPnPq_ldPMx6OVXJr6BAndRjQYMkzyJg/viewform",
                                        "Дружинін В.А." : "https://docs.google.com/forms/d/e/1FAIpQLScYKVG_kj-COnh1l6J91K-7fn8708mCSUeqnaLYkuD32o3NRA/viewform"
                                    },
                                "ВізІнф " : \
                                
                                    {
                                        "Кельник О.І." : "https://docs.google.com/forms/d/e/1FAIpQLSfwBNoIinemZ3LqwZ7L0JwwHMxMA6HM_sNxu3n87M4HiUxIcg/viewform"
                                    },
                                "ТКтОС " : \
                                
                                    {
                                        "Фелінський Г.С." : "https://docs.google.com/forms/d/e/1FAIpQLScgPsYYpMC7lJGOHWGTmkRHxFUHjoLfF6VaeFziggIu_g6xqg/viewform"
                                    },
			},
		}
	}
}
users = \
{
	#"admin" : ['1','кі','ма']
}

courses = ['1','2','3','4']

specs = ['кі','пф','рт']

specsial = \
{
    "кі" : \
    {
        "1" : ["none"],
        "2" : ["none"],
        "3" : ["ма","са"],
        "4" : ["ма","са"]
    },
    "пф" : \
    {
        "1" : ['пфнкт','еф','еітм'],
        "2" : ["none"],
        "3" : ["none"],
        "4" : ['фе','нфне','мрф','крф']
    },
    "рт" : \
    {
        "1" : ['ібтксм','ібтксм(мс)'],
        "2" : ['ібтксм','пазіб(мс)','пазтк(мс)'],
        "3" : ['пазіб'],
        "4" : ['пазіб','пазтк','рзтк']
    }
}

def gen_specs():
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    for i in specs:
        markup.add(InlineKeyboardButton(i.upper(),callback_data="cb_{}".format(i)))
    return markup

def gen_courses():
    markup = InlineKeyboardMarkup()
    for i in courses:
        markup.add(InlineKeyboardButton(i,callback_data="cb_{}".format(i)))
    markup.add(InlineKeyboardButton("<<< Назад",callback_data="cb_back_specs"))
    return markup

def gen_specsials(spec,course):
    markup = InlineKeyboardMarkup()
    for i in specsial[spec][course]:
        markup.add(InlineKeyboardButton(i.upper(),callback_data="cb_{}".format(i)))
    markup.add(InlineKeyboardButton("<<< Назад",callback_data="cb_back_courses"))
    return markup

def getList(course,spec,special):
    text = ""
    for key, val in teachers[spec][course][special].items():
        text += "{}:\n".format(key)
        for k, v in val.items():
            text += "* <a href='{}'>{}</a>\n".format(v,k)
    return text
    

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.from_user.username not in users:
        users.update({call.from_user.username:["1","none","none"]})
    
    print(call.data)
    if call.data[3:].lower() in specs:
        users[call.from_user.username][1] = call.data[3:]
        bot.answer_callback_query(call.id, call.data[3:])
        bot.send_message(call.message.chat.id,"Выберете курс", reply_markup=gen_courses())
    elif call.data[3:].lower() in courses:
        users[call.from_user.username][0] = call.data[3:]
        bot.answer_callback_query(call.id, call.data[3:])
        specialnost = users[call.from_user.username][1]
        curs = users[call.from_user.username][0]
        if specialnost == 'none':
            bot.send_message(call.message.chat.id,"Для начала работы\nВыберите вашу специальность", reply_markup=gen_specs())
        else:
            if specsial[specialnost][curs][0] == "none":
                bot.send_message(chat_id=call.message.chat.id,
                                 text=getList(
                                 users[call.from_user.username][0],
                                 users[call.from_user.username][1],
                                 users[call.from_user.username][2]
                                 ),
                                 parse_mode="HTML",
                                 disable_web_page_preview=True)
            else:
                bot.send_message(call.message.chat.id,"Выберете специализацию", reply_markup=gen_specsials(users[call.from_user.username][1],users[call.from_user.username][0]))
    elif users[call.from_user.username][0] != "none" and \
            users[call.from_user.username][1] != "none" and \
            call.data[3:].lower() in specsial[users[call.from_user.username][1]][users[call.from_user.username][0]]:
        users[call.from_user.username][2] = call.data[3:]
        bot.answer_callback_query(call.id, call.data[3:])
        bot.send_message(chat_id=call.message.chat.id,
                         text=getList(
                             users[call.from_user.username][0],
                             users[call.from_user.username][1],
                             users[call.from_user.username][2]
                             ),
                         parse_mode="HTML",
                         disable_web_page_preview=True)
    elif call.data == "cb_back_courses":
        bot.answer_callback_query(call.id, "<<< Назад")
        users[call.from_user.username][2] = "none"
        bot.send_message(call.message.chat.id,"Выберете курс", reply_markup=gen_courses())
    elif call.data == "cb_back_specs":
        bot.answer_callback_query(call.id, "<<< Назад")
        bot.send_message(call.message.chat.id,"Выберете специальность", reply_markup=gen_specs())
    else:
        bot.send_message(call.message.chat.id,"Для начала работы\nВыберите вашу специальность", reply_markup=gen_specs())
        

@bot.message_handler(func=lambda message: True)
def message_handler(message):
    messageText = message.text.lower()
    users.update({message.from_user.username:["none","none","none"]})
    if messageText == "/start":
        bot.send_message(message.chat.id,"Выберите вашу специальность", reply_markup=gen_specs())
    else:
        bot.send_message(message.chat.id,"Напишите /start для начала работы")
bot.polling(none_stop=True)
