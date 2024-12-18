import reflex as rx

def navbar()->rx.Component:
  return rx.hstack(
      rx.hstack(
        rx.icon(tag="camera"),
        rx.heading("PIXIE",size="6",weight="bold"),
      ),
      rx.hstack(
        rx.link("Inicio",href="/#",size="3",weight="bold"),
        justify="end",
        spacing="5"
      ),
      justify="between",
      align_items="center",
      padding="1em",
      width="100%",
      bg=rx.color("accent",3)
    )