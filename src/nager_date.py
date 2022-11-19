from requests import get


class NagerDate:
	def __init__(self) -> None:
		self.api = "https://date.nager.at/api/v3"
		self.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
		}
	
	def get_country_info(self, county_code: str) -> dict:
		return get(
			f"{self.api}/CountryInfo/{country_code}",
			headers=self.headers).json()
	
	def get_available_countries(self) -> dict:
		return get(
			f"{self.api}/AvailableCountries",
			headers=self.headers).json()
	
	def get_long_weekends(
			self,
			year: int,
			country_code: str) -> dict:
		return get(
			f"{self.api}/LongWeekend/{year}/{country_code}",
			headers=self.headers).json()
	
	def get_public_holidays(
			self,
			year: int,
			country_code: str) -> dict:
		return get(
			f"{self.api}/PublicHolidays/{year}/{country_code}",
			headers=self.headers).json()
	
	def is_today_public_holiday(self, country_code: str) -> int:
		return get(
			f"{self.api}/IsTodayPublicHoliday/{country_code}",
			headers=self.headers).status_code
	
	def get_upcoming_public_holidays(self, country_code: str) -> dict:
		return get(
			f"{self.api}/NextPublicHolidays/{country_code}",
			headers=self.headers).json()
	
	def get_worldwide_upcoming_public_holidays(self) -> dict:
		return get(
			f"{self.api}/NextPublicHolidaysWorldWide",
			headers=self.headers).json()
