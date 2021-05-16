import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo13-addons-oca-stock-logistics-warehouse",
    description="Meta package for oca-stock-logistics-warehouse Odoo addons",
    version=version,
    install_requires=[
        'odoo13-addon-account_move_line_product',
        'odoo13-addon-account_move_line_stock_info',
        'odoo13-addon-procurement_auto_create_group',
        'odoo13-addon-product_quantity_update_force_inventory',
        'odoo13-addon-sale_stock_available_info_popup',
        'odoo13-addon-scrap_reason_code',
        'odoo13-addon-stock_account_change_qty_reason',
        'odoo13-addon-stock_archive_constraint',
        'odoo13-addon-stock_available',
        'odoo13-addon-stock_available_immediately',
        'odoo13-addon-stock_available_unreserved',
        'odoo13-addon-stock_change_qty_reason',
        'odoo13-addon-stock_cubiscan',
        'odoo13-addon-stock_cycle_count',
        'odoo13-addon-stock_demand_estimate',
        'odoo13-addon-stock_demand_estimate_matrix',
        'odoo13-addon-stock_helper',
        'odoo13-addon-stock_inventory_chatter',
        'odoo13-addon-stock_inventory_cost_info',
        'odoo13-addon-stock_inventory_discrepancy',
        'odoo13-addon-stock_inventory_exclude_sublocation',
        'odoo13-addon-stock_inventory_include_exhausted',
        'odoo13-addon-stock_inventory_justification',
        'odoo13-addon-stock_inventory_line_open',
        'odoo13-addon-stock_inventory_lockdown',
        'odoo13-addon-stock_inventory_preparation_filter',
        'odoo13-addon-stock_location_bin_name',
        'odoo13-addon-stock_location_children',
        'odoo13-addon-stock_location_last_inventory_date',
        'odoo13-addon-stock_location_lockdown',
        'odoo13-addon-stock_location_position',
        'odoo13-addon-stock_location_tray',
        'odoo13-addon-stock_location_zone',
        'odoo13-addon-stock_lot_filter_available',
        'odoo13-addon-stock_measuring_device',
        'odoo13-addon-stock_measuring_device_zippcube',
        'odoo13-addon-stock_move_auto_assign',
        'odoo13-addon-stock_move_common_dest',
        'odoo13-addon-stock_move_location',
        'odoo13-addon-stock_mts_mto_rule',
        'odoo13-addon-stock_orderpoint_generator',
        'odoo13-addon-stock_orderpoint_manual_procurement',
        'odoo13-addon-stock_orderpoint_manual_procurement_uom',
        'odoo13-addon-stock_orderpoint_move_link',
        'odoo13-addon-stock_orderpoint_purchase_link',
        'odoo13-addon-stock_orderpoint_route',
        'odoo13-addon-stock_orderpoint_uom',
        'odoo13-addon-stock_packaging_calculator',
        'odoo13-addon-stock_picking_completion_info',
        'odoo13-addon-stock_picking_consolidation_priority',
        'odoo13-addon-stock_picking_procure_method',
        'odoo13-addon-stock_pull_list',
        'odoo13-addon-stock_putaway_product_template',
        'odoo13-addon-stock_quant_manual_assign',
        'odoo13-addon-stock_removal_location_by_priority',
        'odoo13-addon-stock_request',
        'odoo13-addon-stock_request_analytic',
        'odoo13-addon-stock_request_direction',
        'odoo13-addon-stock_request_kanban',
        'odoo13-addon-stock_request_mrp',
        'odoo13-addon-stock_request_picking_type',
        'odoo13-addon-stock_request_purchase',
        'odoo13-addon-stock_request_submit',
        'odoo13-addon-stock_request_tier_validation',
        'odoo13-addon-stock_reserve_rule',
        'odoo13-addon-stock_secondary_unit',
        'odoo13-addon-stock_vertical_lift',
        'odoo13-addon-stock_vertical_lift_empty_tray_check',
        'odoo13-addon-stock_vertical_lift_kardex',
        'odoo13-addon-stock_vertical_lift_packaging_type',
        'odoo13-addon-stock_vertical_lift_server_env',
        'odoo13-addon-stock_vertical_lift_storage_type',
        'odoo13-addon-stock_warehouse_calendar',
        'odoo13-addon-stock_warehouse_orderpoint_stock_info',
        'odoo13-addon-stock_warehouse_orderpoint_stock_info_unreserved',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
