library(tidyverse)

setwd(getwd())

df <- read.csv("movers_by_station_names.csv")


df <- df %>%
  filter(Case_control == 0) %>%
  filter(City == "Toronto")


df$n_movers_in_Lowincome_per <- 100 * df$n_movers_in_Lowincome / df$n_movers_in 
df$n_movers_out_Lowincome_per <- 100 * df$n_movers_out_Lowincome / df$n_movers_out
df$n_stayers_Lowincome_per <- 100 * df$n_stayers_Lowincome / df$n_stayers



selected_stations <- c("Weston", "Bloor", "Don Mills", "Leslie", "Bayview", "Bessarion")


long_data <- df %>%
  filter(stop_label_x %in% selected_stations) %>%
  select(stop_label_x, movers_in_med_income, movers_out_med_income, stayers_med_income) %>%
  filter(
    !is.na(movers_in_med_income),
    !is.na(movers_out_med_income),
    !is.na(stayers_med_income)
  ) %>%
  pivot_longer(
    cols = c(movers_in_med_income, movers_out_med_income, stayers_med_income),
    names_to = "category",
    values_to = "value"
  ) %>%
  mutate(category = factor(category, levels = c(
    "stayers_med_income",
    "movers_in_med_income" , "movers_out_med_income" 
  )))


ggplot(long_data, aes(x = value, y = reorder(stop_label_x, value), fill = category)) +
  geom_col(position = position_dodge2(preserve = "single")) +
  labs(
    x = "Count",
    y = "Station",
    fill = "Category",
    title = "Median income of movers in/out of transit stations (5 years before + 5 after openning)"
  ) +
  scale_fill_manual(
    values = c(
      "movers_in_med_income" = "#6FC7EA",   
      "movers_out_med_income" = "#AB1368",
      "stayers_med_income" = "#F1C500"    
    ),
    labels = c(
      "movers_in_med_income" = "Movers (In)", 
      "movers_out_med_income" = "Movers (Out)", 
      "stayers_med_income" = "Stayers"
    )
  ) +
  xlab("Median annual income") + 
  theme_minimal()











long_data <- df %>%
  filter(stop_label_x %in% selected_stations) %>%
  select(stop_label_x, n_movers_in_Lowincome_per, n_movers_out_Lowincome_per, n_stayers_Lowincome_per) %>%
  filter(
    !is.na(n_movers_in_Lowincome_per),
    !is.na(n_movers_out_Lowincome_per),
    !is.na(n_stayers_Lowincome_per)
  ) %>%
  pivot_longer(
    cols = c(n_movers_in_Lowincome_per, n_movers_out_Lowincome_per, n_stayers_Lowincome_per),
    names_to = "category",
    values_to = "value"
  ) %>%
  mutate(category = factor(category, levels = c(
    "n_movers_in_Lowincome_per",
    "n_movers_out_Lowincome_per" , "n_stayers_Lowincome_per" 
    
  )))


ggplot(long_data, aes(x = value, y = reorder(stop_label_x, value), fill = category)) +
  geom_col(position = position_dodge2(preserve = "single")) +
  labs(
    x = "Count",
    y = "Station",
    fill = "Category",
    title = "Low-income prevalence movers in/out of transit stations (5 years before + 5 after of openning)"
  ) +
  scale_fill_manual(
    values = c(
      "n_movers_in_Lowincome_per" = "#6FC7EA",   
      "n_movers_out_Lowincome_per" = "#AB1368",
      "n_stayers_Lowincome_per" = "#F1C500"    
    ),
    labels = c(
      "n_movers_in_Lowincome_per" = "Movers (In)", 
      "n_movers_out_Lowincome_per" = "Movers (Out)", 
      "n_stayers_Lowincome_per" = "Stayers"
    )
  ) +
  xlab("% low income") + 
  theme_minimal()
