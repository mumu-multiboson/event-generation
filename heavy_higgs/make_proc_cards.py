


from pathlib import Path


def main():
    template_path = Path('proc_card_mg5.tmp')
    for cm_energy in [6, 10, 30]:
        for mass in [500, 600, 700, 800, 900, 1000, 2000, 3000]:
            output_path = Path(f'{cm_energy}tev/{mass}/proc_card_mg5.dat')
            param_card_path = Path(f'{cm_energy}tev/{mass}/param_card.dat').resolve()
            template_text = template_path.read_text()
            template_text = template_text.replace('$MASS', str(mass))
            template_text = template_text.replace('$CM_OVER_2_GEV', str(int(cm_energy * 1000 / 2)))
            template_text = template_text.replace('$PARAM_CARD_PATH', str(param_card_path))
            output_path.write_text(template_text)

            print(f'Created {output_path} with mass {mass} and cm_energy {cm_energy} and param_card {param_card_path}')


if __name__ == "__main__":
    main()