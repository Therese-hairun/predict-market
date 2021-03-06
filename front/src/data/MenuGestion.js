const MenuGestion = [
  {
    text: "manageUsers",
    href: "/listes-des-utilisateurs",
    icon: `
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="12" viewBox="0 0 24 12">
              <path id="Tracé_19688" data-name="Tracé 19688" d="M12,12.75a10.611,10.611,0,0,1,4.24.9A2.984,2.984,0,0,1,18,16.38V18H6V16.39a2.963,2.963,0,0,1,1.76-2.73A10.44,10.44,0,0,1,12,12.75ZM4,13a2,2,0,1,0-2-2A2.006,2.006,0,0,0,4,13Zm1.13,1.1A6.983,6.983,0,0,0,4,14a6.95,6.95,0,0,0-2.78.58A2.011,2.011,0,0,0,0,16.43V18H4.5V16.39A4.5,4.5,0,0,1,5.13,14.1ZM20,13a2,2,0,1,0-2-2A2.006,2.006,0,0,0,20,13Zm4,3.43a2.011,2.011,0,0,0-1.22-1.85,6.8,6.8,0,0,0-3.91-.48,4.5,4.5,0,0,1,.63,2.29V18H24ZM12,6A3,3,0,1,1,9,9,3,3,0,0,1,12,6Z" transform="translate(0 -6)" fill="#fff"/>
            </svg>
            `,
  },
  {
    text: "manageTickets",
    href: "/tous-les-tickets",
    icon: `
              <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18">
                <path id="Tracé_19689" data-name="Tracé 19689" d="M19,3H4.99A2,2,0,0,0,3,5l.01,14A2,2,0,0,0,5,21H15l6-6V5A2.006,2.006,0,0,0,19,3ZM7,8H17v2H7Zm5,6H7V12h5Zm2,5.5V14h5.5Z" transform="translate(-3 -3)" fill="#5c626a"/>
              </svg>
                      `,
  },
  {
    text: "manageCouples",
    href: "/gestion-des-paires",
    icon: `
        <svg class="icon-item" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="5 0 19 24">
          <rect id="Rectangle_1874" data-name="Rectangle 1874" width="24" height="24" fill="none"/>
          <path id="Tracé_19677" class="to-fill" data-name="Tracé 19677" d="M2.88,7.88,4.42,9.42A8.158,8.158,0,0,0,4,12a8,8,0,1,0,8-8,8.158,8.158,0,0,0-2.58.42L7.89,2.89A10,10,0,1,1,2,12,10.11,10.11,0,0,1,2.88,7.88ZM6,12a6,6,0,1,1,6,6A6,6,0,0,1,6,12ZM7,5.5A1.5,1.5,0,1,1,5.5,4,1.5,1.5,0,0,1,7,5.5Z" fill="#5c626a"/>
        </svg>`,
  },
  {
    text: "manageSubscription",
    href: "/gestion-abonnement",
    icon: `

      <svg class="icon-item" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="5 0 19 24">
        <rect id="Rectangle_1872" data-name="Rectangle 1872" width="24" height="24" fill="none"/>
        <path id="Tracé_19674" class="to-fill" data-name="Tracé 19674" d="M11,21H5a2.006,2.006,0,0,1-2-2V5A2.006,2.006,0,0,1,5,3h6Zm2,0h6a2.006,2.006,0,0,0,2-2V12H13Zm8-11V5a2.006,2.006,0,0,0-2-2H13v7Z" fill="#5c626a"/>
        <path id="Tracé_19683" class="to-fill" data-name="Tracé 19683" d="M11,21H5a2.006,2.006,0,0,1-2-2V5A2.006,2.006,0,0,1,5,3h6Zm2,0h6a2.006,2.006,0,0,0,2-2V12H13Zm8-11V5a2.006,2.006,0,0,0-2-2H13v7Z" fill="#5c626a"/>
      </svg>          `,
  },
  {
    text: "discountCode",
    href: "/code-de-reduction",
    icon: `
      <svg xmlns="http://www.w3.org/2000/svg" width="17.272" height="18" viewBox="0 0 17.272 18">
        <path id="Tracé_42553" data-name="Tracé 42553" d="M26.8,9.231a.527.527,0,0,1,0-.466l.671-1.373a1.563,1.563,0,0,0-.674-2.075L25.445,4.6a.528.528,0,0,1-.274-.377l-.264-1.506a1.563,1.563,0,0,0-1.765-1.282l-1.514.214a.527.527,0,0,1-.443-.144L20.086.442a1.562,1.562,0,0,0-2.182,0L16.805,1.5a.528.528,0,0,1-.443.144l-1.514-.214a1.562,1.562,0,0,0-1.765,1.282l-.264,1.506a.528.528,0,0,1-.274.377l-1.35.716a1.563,1.563,0,0,0-.674,2.075l.671,1.373a.527.527,0,0,1,0,.466L10.52,10.6a1.563,1.563,0,0,0,.674,2.075l1.35.716a.527.527,0,0,1,.274.377l.264,1.506a1.562,1.562,0,0,0,1.54,1.3,1.606,1.606,0,0,0,.225-.016l1.514-.214a.527.527,0,0,1,.443.144l1.1,1.063a1.563,1.563,0,0,0,2.182,0l1.1-1.063a.528.528,0,0,1,.443-.144l1.514.214a1.562,1.562,0,0,0,1.765-1.282l.264-1.506a.528.528,0,0,1,.274-.377l1.35-.716a1.563,1.563,0,0,0,.674-2.075Zm-9.879-4.9a1.9,1.9,0,1,1-1.9,1.9A1.905,1.905,0,0,1,16.918,4.326Zm-.982,8.464a.519.519,0,1,1-.734-.734l6.851-6.851a.519.519,0,1,1,.734.734Zm5.135.879a1.9,1.9,0,1,1,1.9-1.9A1.905,1.905,0,0,1,21.071,13.67Z" transform="translate(-10.359 0.002)" fill="#5c626a"/>
      </svg>       
      `,
  },
];

export default MenuGestion;
