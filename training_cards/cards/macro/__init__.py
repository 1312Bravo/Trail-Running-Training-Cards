from importlib import import_module


def _load_card(module_name: str, object_name: str):
    return getattr(import_module(f"{__package__}.{module_name}"), object_name)


mainstream_return_to_consistency = _load_card("mainstream_endurance.mainstream_return_to_consistency", "mainstream_return_to_consistency")
mainstream_base_development = _load_card("mainstream_endurance.mainstream_base_development", "mainstream_base_development")
mainstream_capacity_development = _load_card("mainstream_endurance.mainstream_capacity_development", "mainstream_capacity_development")
mainstream_race_specific_preparation = _load_card("mainstream_endurance.mainstream_race_specific_preparation", "mainstream_race_specific_preparation")
mainstream_peak_and_taper = _load_card("mainstream_endurance.mainstream_peak_and_taper", "mainstream_peak_and_taper")
mainstream_competition_management = _load_card("mainstream_endurance.mainstream_competition_management", "mainstream_competition_management")
mainstream_recovery_and_transition = _load_card("mainstream_endurance.mainstream_recovery_and_transition", "mainstream_recovery_and_transition")
mainstream_off_season = _load_card("mainstream_endurance.mainstream_off_season", "mainstream_off_season")
mainstream_maintenance = _load_card("mainstream_endurance.mainstream_maintenance", "mainstream_maintenance")
endurance_80_20_base_development = _load_card("80_20_endurance.endurance_80_20_base_development", "endurance_80_20_base_development")
endurance_80_20_capacity_development = _load_card("80_20_endurance.endurance_80_20_capacity_development", "endurance_80_20_capacity_development")
endurance_80_20_race_specific_preparation = _load_card("80_20_endurance.endurance_80_20_race_specific_preparation", "endurance_80_20_race_specific_preparation")
endurance_80_20_competition_management = _load_card("80_20_endurance.endurance_80_20_competition_management", "endurance_80_20_competition_management")
endurance_80_20_maintenance = _load_card("80_20_endurance.endurance_80_20_maintenance", "endurance_80_20_maintenance")
lydiard_base_development = _load_card("lydiard.lydiard_base_development", "lydiard_base_development")
lydiard_capacity_development = _load_card("lydiard.lydiard_capacity_development", "lydiard_capacity_development")
lydiard_race_specific_preparation = _load_card("lydiard.lydiard_race_specific_preparation", "lydiard_race_specific_preparation")
lydiard_peak_and_taper = _load_card("lydiard.lydiard_peak_and_taper", "lydiard_peak_and_taper")
cts_base_development = _load_card("cts.cts_base_development", "cts_base_development")
cts_capacity_development = _load_card("cts.cts_capacity_development", "cts_capacity_development")
cts_race_specific_preparation = _load_card("cts.cts_race_specific_preparation", "cts_race_specific_preparation")
cts_competition_management = _load_card("cts.cts_competition_management", "cts_competition_management")
evoke_base_development = _load_card("evoke_endurance.evoke_base_development", "evoke_base_development")
evoke_capacity_development = _load_card("evoke_endurance.evoke_capacity_development", "evoke_capacity_development")
evoke_race_specific_preparation = _load_card("evoke_endurance.evoke_race_specific_preparation", "evoke_race_specific_preparation")
swap_return_to_consistency = _load_card("swap.swap_return_to_consistency", "swap_return_to_consistency")
swap_base_development = _load_card("swap.swap_base_development", "swap_base_development")
swap_capacity_development = _load_card("swap.swap_capacity_development", "swap_capacity_development")
swap_race_specific_preparation = _load_card("swap.swap_race_specific_preparation", "swap_race_specific_preparation")
swap_competition_management = _load_card("swap.swap_competition_management", "swap_competition_management")
swap_off_season = _load_card("swap.swap_off_season", "swap_off_season")
sharman_race_specific_preparation = _load_card("sharman_ultra.sharman_race_specific_preparation", "sharman_race_specific_preparation")
sharman_competition_management = _load_card("sharman_ultra.sharman_competition_management", "sharman_competition_management")

MACRO_CARDS = [
    mainstream_return_to_consistency,
    mainstream_base_development,
    mainstream_capacity_development,
    mainstream_race_specific_preparation,
    mainstream_peak_and_taper,
    mainstream_competition_management,
    mainstream_recovery_and_transition,
    mainstream_off_season,
    mainstream_maintenance,
    endurance_80_20_base_development,
    endurance_80_20_capacity_development,
    endurance_80_20_race_specific_preparation,
    endurance_80_20_competition_management,
    endurance_80_20_maintenance,
    lydiard_base_development,
    lydiard_capacity_development,
    lydiard_race_specific_preparation,
    lydiard_peak_and_taper,
    cts_base_development,
    cts_capacity_development,
    cts_race_specific_preparation,
    cts_competition_management,
    evoke_base_development,
    evoke_capacity_development,
    evoke_race_specific_preparation,
    swap_return_to_consistency,
    swap_base_development,
    swap_capacity_development,
    swap_race_specific_preparation,
    swap_competition_management,
    swap_off_season,
    sharman_race_specific_preparation,
    sharman_competition_management,
]
