import random
import math
import pandas as pd
import numpy as np

station_data = pd.read_csv("case-study-data.csv")

overall_results = []

for station in ["Cooksville", "Panama",	"McKernan-Belgravia", "Arbutus", "Northfield"]:

	for scenario in ["scenario1", "scenario2","scenario3"]:

		# station = "Cooksville"
		# scenario = "scenario1"

		station_attributes = {
			"name": station,
			"year_open": station_data.loc[station_data["variable"] == "year_open", station].iloc[0],
			"population": station_data.loc[station_data["variable"] == "population", station].iloc[0], 
			"dwellings_total": station_data.loc[station_data["variable"] == "dwellings", station].iloc[0],
			"age": {
				"age_0_4":  station_data.loc[station_data["variable"] == "age_0_4", station].iloc[0],
				"age_5_9":  station_data.loc[station_data["variable"] == "age_5_9", station].iloc[0],
				"age_10_14": station_data.loc[station_data["variable"] == "age_10_14", station].iloc[0],
				"age_15_19": station_data.loc[station_data["variable"] == "age_15_19", station].iloc[0],
				"age_20_24": station_data.loc[station_data["variable"] == "age_20_24", station].iloc[0],
				"age_25_29": station_data.loc[station_data["variable"] == "age_25_29", station].iloc[0],
				"age_30_34": station_data.loc[station_data["variable"] == "age_30_34", station].iloc[0],
				"age_35_39": station_data.loc[station_data["variable"] == "age_35_39", station].iloc[0],
				"age_40_44": station_data.loc[station_data["variable"] == "age_40_44", station].iloc[0],
				"age_45_49": station_data.loc[station_data["variable"] == "age_45_49", station].iloc[0],
				"age_50_54": station_data.loc[station_data["variable"] == "age_50_54", station].iloc[0],
				"age_55_59": station_data.loc[station_data["variable"] == "age_55_59", station].iloc[0],
				"age_60_64": station_data.loc[station_data["variable"] == "age_60_64", station].iloc[0],
				"age_65_69": station_data.loc[station_data["variable"] == "age_65_69", station].iloc[0],
				"age_70_74": station_data.loc[station_data["variable"] == "age_70_74", station].iloc[0],
				"age_75_79": station_data.loc[station_data["variable"] == "age_75_79", station].iloc[0],
				"age_80_84": station_data.loc[station_data["variable"] == "age_80_84", station].iloc[0],
				"age_85_100": station_data.loc[station_data["variable"] == "age_85_100", station].iloc[0]
			},
			"sex": {
				"sex_m": station_data.loc[station_data["variable"] == "sex_m", station].iloc[0],
				"sex_f": station_data.loc[station_data["variable"] == "sex_f", station].iloc[0]
			},
			"low_inc": {
				"low_inc_yes": station_data.loc[station_data["variable"] == "low_inc_yes", station].iloc[0],
				"low_inc_no": station_data.loc[station_data["variable"] == "low_inc_no", station].iloc[0]
			},
			"marital": {
				"marital_yes": station_data.loc[station_data["variable"] == "married_yes", station].iloc[0],
				"marital_no": station_data.loc[station_data["variable"] == "married_no", station].iloc[0]
			},
			"built_pre": {
				"built_pre_avgbedrooms": station_data.loc[station_data["variable"] == "existing_avgbedrooms", station].iloc[0],
				"built_pre_singledetached": station_data.loc[station_data["variable"] == "existing_singledetached", station].iloc[0],
				"built_pre_rowtownsemi": station_data.loc[station_data["variable"] == "existing_rowtownsemi", station].iloc[0],
				"built_pre_aptsmall": station_data.loc[station_data["variable"] == "existing_aptsmall", station].iloc[0],
				"built_pre_aptlarge": station_data.loc[station_data["variable"] == "existing_aptlarge", station].iloc[0]
			},
			"built_change": {
				# these were done in 0%-100% in the base model, not 0-1
				"built_change_avgbedrooms": station_data.loc[station_data["variable"] == scenario + "_avgbedrooms_percchange", station].iloc[0],
				"built_change_dwellings": station_data.loc[station_data["variable"] == scenario + "_totaldwellings_percchange", station].iloc[0],
				"built_change_singledetached": station_data.loc[station_data["variable"] == scenario + "_singledetached_percchange", station].iloc[0],
				"built_change_rowtownsemi": station_data.loc[station_data["variable"] == scenario + "_rowtownsemi_percchange", station].iloc[0],
				"built_change_aptsmall": station_data.loc[station_data["variable"] == scenario + "_aptsmall_percchange", station].iloc[0],
				"built_change_aptlarge": station_data.loc[station_data["variable"] == scenario + "_aptlarge_percchange", station].iloc[0]
			}
		}


		def samplePerson():

			p_yes = station_attributes["low_inc"]["low_inc_yes"]
			r = random.random()
			low_inc = int(r < p_yes)

			p_yes = station_attributes["sex"]["sex_f"]
			r = random.random()
			sex = int(r < p_yes)

			age_probs = station_attributes["age"]
			age_group = random.choices(
				population=list(age_probs.keys()),
				weights=list(age_probs.values()),
				k=1
			)[0]
			parts = age_group.replace("age_", "").split("_")
			low, high = map(int, parts)
			age = random.randint(low, high)

			p_yes = station_attributes["marital"]["marital_yes"]
			r = random.random()
			marital = int(r < p_yes)
			if age_group == "age_0_4" or age_group == "age_5_9" or age_group == "age_10_14" or age_group == "age_15_19" or age_group == "age_20_24":
				marital = int(False)

			return {
				"age": age, # numeric
				"sex": sex, # 1 (female) or 0 (male)
				"low_inc": low_inc, # 1 (yes) or 0 (no)
				"marital": marital # 1 (married) or 0 (not married)
			}
			
		def simulateMovingIndividual(sample_person):

			b_intercept = 29.9305
			
			b_age = -0.0267
			x_age = sample_person["age"]
			
			b_sex = -0.0248
			x_sex = sample_person["sex"]

			b_low_inc = 0.2745
			x_low_inc = sample_person["low_inc"]

			b_marital = -0.0342
			x_marital = sample_person["marital"]

			b_year = -0.0142
			x_year = station_attributes["year_open"]

			b_built_pre_avgbedrooms = -0.0325
			x_built_pre_avgbedrooms = (
				station_attributes["built_pre"]["built_pre_avgbedrooms"]
			)

			b_built_pre_singledetached = 0.0004
			x_built_pre_singledetached = (
				station_attributes["dwellings_total"] * station_attributes["built_pre"]["built_pre_singledetached"]
			)

			b_built_pre_rowtownsemi = 0.0001
			x_built_pre_rowtownsemi = (
				station_attributes["dwellings_total"] * station_attributes["built_pre"]["built_pre_rowtownsemi"]
			)

			b_built_pre_aptsmall = 0.0001
			x_built_pre_aptsmall = (
				station_attributes["dwellings_total"] * station_attributes["built_pre"]["built_pre_aptsmall"]
			)

			b_built_pre_aptlarge = 0.0000
			x_built_pre_aptlarge = (
				station_attributes["dwellings_total"] * station_attributes["built_pre"]["built_pre_aptlarge"]
			)

			b_built_change_avgbedrooms = 0.0282
			x_built_change_avgbedrooms = (
				station_attributes["built_change"]["built_change_avgbedrooms"]
			)

			b_built_change_dwellings = 0.00003
			x_built_change_singledetached = (
				station_attributes["built_change"]["built_change_dwellings"]
			)

			b_built_change_singledetached = -0.0009
			x_built_change_singledetached = (
				station_attributes["built_change"]["built_change_singledetached"]
			)

			b_built_change_rowtownsemi = -0.0001
			x_built_change_rowtownsemi = (
				station_attributes["built_change"]["built_change_rowtownsemi"]
			)

			b_built_change_aptsmall = 0.0001
			x_built_change_aptsmall = (
			station_attributes["built_change"]["built_change_aptsmall"]
			)

			b_built_change_aptlarge = 0.0001
			x_built_change_aptlarge = (
				station_attributes["built_change"]["built_change_aptlarge"]
			)

			b_built_change_dwe_X_bedrooms = -0.0006
			
			z = (
				b_intercept + 
				b_low_inc * x_low_inc + 
				b_age * x_age + 
				b_year * x_year + 
				b_sex * x_sex + 
				b_marital * x_marital + 
				b_built_pre_avgbedrooms * x_built_change_avgbedrooms + 
				b_built_pre_singledetached * x_built_pre_singledetached + 
				b_built_pre_rowtownsemi * x_built_pre_rowtownsemi + 
				b_built_pre_aptsmall * x_built_pre_aptsmall + 
				b_built_pre_aptlarge * x_built_pre_aptlarge +
				b_built_change_avgbedrooms * x_built_change_avgbedrooms +
				b_built_change_singledetached * x_built_change_singledetached + 
				b_built_change_rowtownsemi * x_built_change_rowtownsemi + 
				b_built_change_aptsmall * x_built_change_aptsmall + 
				b_built_change_aptlarge * x_built_change_aptlarge + 
				b_built_change_dwe_X_bedrooms * b_built_change_dwellings * b_built_change_avgbedrooms
			)
			
			p = 1 / (1 + math.exp(-z))

			r = random.random()
			move = int(r < p)
			
			return p, move



		# similate every person, do so ~10 times to get an average



		summaries = []

		i = 0
		while i < 100:

			results = []
			j = 0
			while j < station_attributes["population"]:
				j += 1
				sample_person = samplePerson()
				move = simulateMovingIndividual(sample_person)
				result = sample_person
				result["move_p"] = move[0]
				result["move_b"] = move[1]
				results.append(result)
			df = pd.DataFrame(results)


			by_low_inc = (
				df.groupby("low_inc", as_index=False)
				.agg(
					total_people=("move_b", "count"),
					total_moved=("move_b", "sum"),
					percent_moved=("move_b", "mean")
				)
			)

			summaries.append(by_low_inc)

			i += 1


		combined = pd.concat(summaries)


		average_summary = (
			combined.groupby("low_inc", as_index=False)
			.agg(
				avg_total_people=("total_people", "mean"),
				avg_total_moved=("total_moved", "mean"),
				avg_percent_moved=("percent_moved", "mean")
			)
		)

		average_summary["scenario"] = scenario
		average_summary["station"] = station

		overall_results.append(average_summary)


overall_results = pd.concat(overall_results)

print(overall_results)
