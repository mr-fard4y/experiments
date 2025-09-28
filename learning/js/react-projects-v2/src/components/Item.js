
function Item(data) {
  return (
    <div>
      <h3>{data.name}</h3>
      <img src={data.image} alt={data.name} width='300' />
      <p>{'Origin: ${data.origin && data.origin.name}'}</p>
    </div>
  )
};

export default Item;
