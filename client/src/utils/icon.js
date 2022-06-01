import computo from "../assets/categories/computo.png";
import electronico from "../assets/categories/electronico.png";
import accesorios from "../assets/categories/accesoriosPersonales.png";
import documentos from "../assets/categories/documentos.png";
import libros from "../assets/categories/libros.png";
import papeleria from "../assets/categories/papeleria.png";
import prenda from "../assets/categories/prendas.png";
import willSmith from "../assets/categories/otro.png";

export function iconSelector(category) {
  if (category == "Cómputo") {
    return computo;
  } else if (category == "Electrónico") {
    return electronico;
  } else if (category == "Accesorios Personales") {
    return accesorios;
  } else if (category == "Documentos") {
    return documentos;
  } else if (category == "Libros") {
    return libros;
  } else if (category == "Papelería") {
    return papeleria;
  } else if (category == "Prendas") {
    return prenda;
  } else {
    return willSmith;
  }
}
